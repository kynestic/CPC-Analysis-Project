import time
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import ast
import numpy as np

start_time = time.time()
df = pd.read_csv(r'data\processed\stock_news_price.csv')

tfidf_results = pd.DataFrame()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    print(index)
    events_list = eval(row['events'])

    tfidf_vectorizer = TfidfVectorizer()

    events_matrix = tfidf_vectorizer.fit_transform(events_list)

    max_vector = np.max(events_matrix.toarray(), axis=0)

    tfidf_df = pd.DataFrame([max_vector], columns=tfidf_vectorizer.get_feature_names_out())
    tfidf_results = pd.concat([tfidf_results, tfidf_df], ignore_index=True)


tfidf_results.fillna(0, inplace=True)
if len(df['events']) != len(tfidf_results):
    df['events'] = tfidf_results
else:
    print(len(df['events']))
    print(len(tfidf_results))
    tfidf_results['timestamp'] = df['timestamp']
    tfidf_results.to_csv(r'data\embedding_text\IF-IDF_EmbeddingText.csv', index=False)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")