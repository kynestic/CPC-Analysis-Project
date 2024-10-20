import pandas as pd

df1 = pd.read_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\embedding_text\BERT_EmbeddingText.csv')
df2 = pd.read_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\raw\stock_news_price.csv')

df1['timestamp'] = df2['timestamp']

df1.to_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\embedding_text\BERT_EmbeddingText.csv', index=False)