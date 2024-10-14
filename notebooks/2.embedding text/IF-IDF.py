from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import ast

df = pd.read_csv(r'data\processed\stock_news_price.csv')

tfidf_results = pd.DataFrame()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    events_list = eval(row['events']) 

    tfidf_vectorizer = TfidfVectorizer()
    
    events_matrix = tfidf_vectorizer.fit_transform(events_list)

    tfidf_df = pd.DataFrame(events_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    tfidf_results = pd.concat([tfidf_results, tfidf_df], ignore_index=True)

# Save the resulting DataFrame to a CSV file
tfidf_results.fillna(0, inplace=True)
tfidf_results.to_csv('data/processed/news_vector.csv', index=False)
print("TF-IDF features extracted and saved to news_vector.csv")