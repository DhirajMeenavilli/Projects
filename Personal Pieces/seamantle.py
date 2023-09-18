import gensim
import math
import pandas as pd
import gensim.downloader as api
import numpy as np
from gensim.models.keyedvectors import KeyedVectors
from english_words import english_words_lower_set as words
# except:
#     import pip 
#     pip.main(['install','pyspellchecker'])

# wv = api.load('word2vec-google-news-300')
wv = KeyedVectors.load_word2vec_format('betterDict.txt', binary=False)

# df = pd.DataFrame
words = []
vectors = []
i = 0
for index,word in enumerate(wv.index_to_key):
    a_word = True
    if len(word) > 3 and word[0] == word[1] == word[2]:
        a_word = False
        
    if word.isalpha() and word.lower() == word and len(word) > 3 and word.lower() != word.upper() and a_word:
        words.append(word)
        vectors.append(wv.vectors[wv.get_index(word)])

df = pd.DataFrame(np.array(vectors),index=words)

np.savetxt('betterDict.txt', df.reset_index().values, 
           delimiter=" ", 
           header="{} {}".format(len(df), len(df.columns)),
           comments="",
           fmt=["%s"] + ["%.18e"]*len(df.columns))

i = 0
fil = open('test.txt','w')
for index,word in enumerate(wv.index_to_key):
    closest = wv.most_similar(word,topn=1)
    fil.write(word + ' ' + closest[0][0] + ' ' + str(closest[0][1]) + '\n')
fil.close()

data = pd.read_csv('test.txt',sep = " ", header = None)
data.columns = ['word','closest','simmilarity']

print(data.loc[data['word'] == 'precious'])
wv.most_similar('limited',topn=1)

df = data.loc[data['simmilarity'] > 0.58545]
df = df.loc[data['simmilarity'] <= 0.58555]
df.sort_values(by=['simmilarity'])