'''Parse and format raw data.'''

import pandas as pd

if __name__ == '__main__':

    # Load the raw data
    datasets = [pd.read_csv('../data/raw_data/twitter-2016dev-CE.txt', sep='\t')]
    datasets.append(pd.read_csv('../data/raw_data/twitter-2016devtest-CE.txt', sep='\t'))
    datasets.append(pd.read_csv('../data/raw_data/twitter-2016test-CE.txt', sep='\t'))
    datasets.append(pd.read_csv('../data/raw_data/twitter-2016train-CE.txt', sep='\t'))

    # Concatenate the datasets
    df = pd.concat(datasets, ignore_index=True)
    print(df.head())

    # Save the formatted data
    df.to_parquet('../data//twitter-2016.parquet', index=False)
    