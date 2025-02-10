from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl")

input_text = "Q: Is the text: 'I've lived in the City of Edmonton my whole life and have never seen this level of ignorance and incompetence before. From unfinished projects to unexplained delays in construction, LRT, bridges, road construction and more. Graffiti needs to be dealt with. There is NO accountability to the taxpayer. Council is definitely not in touch with the residents. There have been many decisions made without consulting the residents yay are really affected. NO grass roots planning.'about the topic of Cost of living?. A: Yes or No"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))