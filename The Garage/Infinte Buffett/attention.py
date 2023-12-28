import torch
import torch.nn as nn

class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__() # I've never seen this kind of inheritience of self refrence.
        self.embed_size = embed_size
        self.heads = heads 
        self.head_dim = embed_size // heads # Embed size always has to be a multiple of heads

        assert(embed_size % heads == 0), "Embed Size is not a multiple of heads, cannot cleanly split." 


        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fully_connected_out = nn.Linear(heads*self.head_dim, embed_size)

    def forward(self, values, keys, query, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        #Split the embedding into self.heads pieces

        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = query.reshape(N, query_len, self.heads, self.head_dim)

        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys]) # matrix multiplication with multiple dimensions
        # Query Shape (N, query_len, heads, heads_dim), Keys shape (N, key_len, heads, heads_dim)
        # Energy shape (N, heads, query_len, key_len)

        if mask:
            energy = energy.masked_fill(mask == 0, float("-1e15"))
        
        attention = torch.softmax(energy/(self.embed_size**(1/2)), dim=3)

        out = torch.einsum("nhqk,nkhd->nqhd",[attention,values])
        # Attention: (N, heads, query_len, key_len)
        # Values: (N, key_len, heads, heads_dim)
        # Out: (N, query_len, heads, head_dim)

        out.reshape(N, query_len, self.heads*self.head_dim)

        out = self.fully_connected_out(out)
        return out
    
class TransformerBlock(nn.module):
    def __init__(self,embed_size, heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = SelfAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(embed_size) # Takes an average for every example
        self.norm1 = nn.LayerNorm(embed_size) # Takes an average for every example

        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, forward_expansion*embed_size),
            nn.ReLU(),
            nn.Linear(forward_expansion*embed_size, embed_size)
            )
        
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, value, key, query, mask):
       
        attention = self.attention(value, key, query, mask)
        x = self.dropout(self.norm1(attention + query)) # Why are we adding?
       
        forward = self.feed_forward(x)
        out = self.dropout(self.norm2(forward + x))
       
        return out