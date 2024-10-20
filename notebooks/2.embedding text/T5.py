import torch
import time
from transformers import T5Tokenizer, T5EncoderModel
import numpy as np
import pandas as pd

start_time = time.time()
# Use T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-base", cache_dir='./model_cache')
# Use the T5EncoderModel instead of T5Model
model = T5EncoderModel.from_pretrained("t5-base", cache_dir='./model_cache')

# Read the dataset
df = pd.read_csv(r'data\processed\stock_news_price.csv')

embedding_text = []
line = 0
print(df)

# Loop through each event
for item in df['events']:
    line += 1
    print(line)
    # Tokenize the event
    inputs = tokenizer(item, return_tensors='pt', padding=True, truncation=True)
    # Get the embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the last hidden state
    event_embedding = outputs.last_hidden_state.mean(dim=1).cpu().numpy().reshape(-1) # Shape: (1, hidden_size)

    # Stack embeddings for all events and calculate the mean
    embedding_text.append(event_embedding)

# Save the result
data = pd.DataFrame(embedding_text)
data['timestamp'] = df['timestamp']
data.to_csv(r'data\embedding_text\T5_EmbeddingText.csv', index=False)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")