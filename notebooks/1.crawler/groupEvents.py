from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import ast

df = pd.read_csv('stock_news_price_after.csv')

df = df.groupby(['timestamp','open','high','low','close','Adj close','volume']).agg({
    'events': lambda x: list(x)
}).reset_index()
df['events'] = df['events'].apply(ast.literal_eval)
df.to_csv('data\processed\stock_news_price.csv', index=False)
print(df)