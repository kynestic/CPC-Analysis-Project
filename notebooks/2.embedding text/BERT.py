import torch
from transformers import BERTModel, BERTTokenizer
import numpy as np
import pandas as pd

tokenizer = BERTTokenizer.from_pretrained("bert-base-uncased", cache_dir='./model_cache')
model = BERTModel.from_pretrained("bert-base-uncased", cache_dir='./model_cache')

df = pd.read_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\processed\stock_news_price.csv')

embedding_text = []
line = 0
print(df)
for item in df['events']:
    line+=1
    print(line)
    events_embedding = []
    list_item = list(item)

    for event in list_item:
        inputs = tokenizer(event, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        event_embedding = outputs.pooler_output.cpu().numpy()
        events_embedding.append(events_embedding)
    
    events_embedding = np.vstack(events_embedding)
    mean_events_embedding = np.mean(events_embedding, axis=0)
    embedding_text.append(mean_events_embedding)

data = pd.DataFrame(embedding_text)
data.to_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\raw\CLIP_EmbeddingText.csv', index=False)