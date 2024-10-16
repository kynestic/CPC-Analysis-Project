import torch
from transformers import CLIPModel, CLIPTokenizer
import numpy as np

tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch16")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")

events = [
    "Self-driving cars are becoming more popular.",
    "Stock prices are fluctuating due to market volatility.",
    "New AI models are improving natural language processing."
]

events_embedding = []

for event in events:
    inputs = tokenizer(event, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        event_embedding = model.get_text_features(**inputs)
    events_embedding.append(event_embedding.cpu().numpy())

events_embedding = np.vstack(events_embedding)

mean_events_embedding = np.mean(events_embedding, axis=0)

print("Vector trung bình đại diện cho ngày:", mean_events_embedding)