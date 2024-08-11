import pandas as pd

def anonymize(path='reviews_small.csv', save_path='reviews_anonymized.csv', columns=['User', 'Release', 'Band']):
    df = pd.read_csv(path)
    current_idx = 0
    for col in columns:
        name_to_idx = {item: i + current_idx for i, item in enumerate(df[col].unique())}
        df[col] = df[col].apply(lambda x: name_to_idx[x])  # Store the transformed column back into the DataFrame
        current_idx += len(name_to_idx)
    df.to_csv(save_path, index=False)

if __name__ == '__main__':  # Corrected the condition
    print("Anonymizing Entries...")
    anonymize()
