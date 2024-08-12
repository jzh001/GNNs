import pandas as pd
from collections import Counter

def anonymize(path='reviews_full_v10-1.csv', 
              save_path='reviews_anonymized.csv', 
              anon_columns=['User', 'Release'],
              columns = ['User', 'Release', 'Combined_Genre', 'Score', 'Cleansed Text'],
              thresholds = {
                  'User': 10,
                  'Release': 10,
              }
              ):
    df = pd.read_csv(path)
    df = df[columns]
    df = filter_df(df, thresholds)
    current_idx = 0
    for col in anon_columns:
        name_to_idx = {item: i + current_idx for i, item in enumerate(df[col].unique())}
        df[col] = df[col].apply(lambda x: name_to_idx[x])
        current_idx += len(name_to_idx)
    df.to_csv(save_path, index=False)

def filter_df(df, thresholds):
    for col in thresholds:
        col_count = Counter(df[col])
        filtered = set([x for x in col_count if col_count[x] > thresholds[col]])
        filtered_idx = [True if x in filtered else False for x in df[col]]
        df = df[filtered_idx]
    df = df.reset_index(drop=True)
    return df

if __name__ == '__main__': 
    print("Anonymizing Entries...")
    anonymize()
