import torch
import time
from transformers import BertModel, BertTokenizer  # Correct import from transformers
import numpy as np
import pandas as pd

start_time = time.time()
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", cache_dir='./model_cache')
model = BertModel.from_pretrained("bert-base-uncased", cache_dir='./model_cache')

df = pd.read_csv(r'data\processed\stock_news_price.csv')

embedding_text = []
line = 0

for item in df['events']:
    line += 1
    print(f"Processing line {line}")
    
    events_embedding = []

    inputs = tokenizer(item, return_tensors='pt', padding=True, truncation=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
        
    event_embedding = outputs.pooler_output.cpu().numpy() 
    
    events_embedding.append(event_embedding)

    events_embedding = np.vstack(events_embedding)
    mean_events_embedding = np.mean(events_embedding, axis=0)
    
    embedding_text.append(mean_events_embedding)

data = pd.DataFrame(embedding_text)
data['timestamp'] = df['timestamp']
data.to_csv(r'data\embedding_text\BERT_EmbeddingText.csv', index=False)
print("Embeddings saved to BERT_EmbeddingText.csv")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")