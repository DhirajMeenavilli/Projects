import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import  AutoModelForSequenceClassification, AutoTokenizer, AutoConfig

class SatisfactionDataset(Dataset): # Not sure what the Dataset class is or does
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    
    def __getitem__(self, index):
        item = {'input_ids':torch.tensor(self.encodings['input_ids'][index]), 
                'attention_mask':torch.tensor(self.encodings['attention_mask'][index]),
                'labels': torch.tensor(self.labels[index])}
        
        return item
    
    def __len__(self):
        return len(self.encodings)

    def getAll(self):
        return {'input_ids':torch.tensor(self.encodings['input_ids']),'attention_mask':torch.tensor(self.encodings['attention_mask']), 'labels': torch.tensor(self.labels)}

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']

df = pd.read_csv("CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv", index_col=0)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path="facebook/bart-large-mnli") # Not sure how this tokenizer works

fold_1, fold1_labels = [str(i) for i in df['a2'][:150].values], df[candidateLabels][:150].values
fold_2, fold2_labels = [str(i) for i in df['a2'][150:300].values], df[candidateLabels][150:300].values
fold_3, fold3_labels = [str(i) for i in df['a2'][300:450].values], df[candidateLabels][300:450].values
fold_4, fold4_labels = [str(i) for i in df['a2'][450:600].values], df[candidateLabels][450:600].values
fold_5, fold5_labels = [str(i) for i in df['a2'][600:750].values], df[candidateLabels][600:750].values



for i in range(5):
    print(i)
    config = AutoConfig.from_pretrained("facebook/bart-large-mnli") # We reinstantiate the model everytime allowing us to retrain and thus get our different models

    num_labels = 30  
    config.num_labels = num_labels
    config.problem_type = "multi_label_classification"

    model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli",config=config,ignore_mismatched_sizes=True) 

    model.train()

    if i == 0:
        train_texts, train_labels = fold_1 + fold_2 + fold_3 + fold_4, fold1_labels + fold2_labels + fold3_labels + fold4_labels #Not sure why I need to stringify the texts
        test_texts, test_labels = fold_5, fold5_labels

    if i == 1:
        train_texts, train_labels = fold_1 + fold_2 + fold_3 + fold_5, fold1_labels + fold2_labels + fold3_labels + fold5_labels #Not sure why I need to stringify the texts
        test_texts, test_labels = fold_4, fold4_labels
    
    if i == 2:
        train_texts, train_labels = fold_1 + fold_2 + fold_4 + fold_5, fold1_labels + fold2_labels + fold4_labels + fold5_labels #Not sure why I need to stringify the texts
        test_texts, test_labels = fold_3, fold3_labels

    if i == 3:
        train_texts, train_labels = fold_1 + fold_3 + fold_4 + fold_5, fold1_labels + fold3_labels + fold4_labels + fold5_labels #Not sure why I need to stringify the texts
        test_texts, test_labels = fold_2, fold2_labels
    
    if i == 4:
        train_texts, train_labels = fold_2 + fold_3 + fold_4 + fold_5, fold2_labels + fold3_labels + fold4_labels + fold5_labels #Not sure why I need to stringify the texts
        test_texts, test_labels = fold_1, fold1_labels

    train_encodings = tokenizer(train_texts, truncation=True, padding=True) # Not sure why the encodings are instances of the tokenizer class
    test_encodings = tokenizer(test_texts, truncation=True, padding=True)

    train_dataset = SatisfactionDataset(train_encodings, train_labels)
    test_dataset = SatisfactionDataset(test_encodings, test_labels)

    train_loader = DataLoader(train_dataset, batch_size=15, shuffle=True)

    optim = AdamW(model.parameters(), lr=2e-5)

    num_epochs = 5
    for epoch in range(num_epochs):
        total_loss = 0
        for batch in train_loader:

            optim.zero_grad() # Not sure what exactly this does as a function. Could be just exactly zeroing out the gradients

            outputs = model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'], labels=batch['labels'].to(dtype=torch.float))
            # print(outputs)
            loss = outputs[0]
            # print(loss)
            total_loss += loss.item()

            loss.backward()
            optim.step()
        
        print(f'Epoch {epoch + 1}/{num_epochs}, Training Loss: {total_loss}')

    model.eval()

    with torch.no_grad():
        test = test_dataset.getAll()
        test_outputs = model(input_ids=test['input_ids'], attention_mask=test['attention_mask'],labels=test['labels'].to(dtype=torch.float))
        print(test_outputs)
        test_loss = test_outputs[0]

    print(f'The loss is, {test_loss}')


# Need to implement evaluation.

# tok = tokenizer([str(i) for i in df['a2'][:3].values], truncation=True, padding=True)
# test_data = SatisfactionDataset(tok, df[candidateLabels][:3].values)
# train_loader = DataLoader(test_data)
# for batch in train_loader:
#     print(model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'], labels=batch['labels'].to(dtype=torch.float)))