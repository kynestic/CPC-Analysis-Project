import torch
import time
from transformers import CLIPModel, CLIPTokenizer  # Correct import from transformers
import numpy as np
import pandas as pd

start_time = time.time()
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32", cache_dir='./model_cache')
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32", cache_dir='./model_cache')

df = pd.read_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\raw\stock_news_price.csv')

embedding_text = []
line = 0

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

for item in df['events']:
    line += 1
    print(f"Processing line {line}")
    
    events_embedding = []

    inputs = tokenizer(text=item, return_tensors='pt', padding=True, truncation=True)
    
    with torch.no_grad():
        outputs = model.get_text_features(**inputs)
        
    event_embedding = outputs.cpu().numpy().reshape(-1)

    embedding_text.append(event_embedding)

data = pd.DataFrame(embedding_text)
data['timestamp'] = df['timestamp']
data.to_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\embedding_text\CLIP_EmbeddingText.csv', index=False)
print("Embeddings saved to CLIP_EmbeddingText.csv")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")