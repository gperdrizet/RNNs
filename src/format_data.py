'''Parse and format raw data.'''

# Standard library
from pathlib import Path

# Third-party
import pandas as pd


if __name__ == '__main__':

    # Set data path relative to this file's location
    DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
    RAW_DATA_DIR = DATA_DIR / 'raw_data'

    # Load the raw data
    column_names = ['id', 'name', 'score', 'text']
    datasets = [pd.read_csv(RAW_DATA_DIR / 'twitter-2016dev-CE.txt', sep='\t', header=None, names=column_names)]
    datasets.append(pd.read_csv(RAW_DATA_DIR / 'twitter-2016devtest-CE.txt', sep='\t', header=None, names=column_names))
    datasets.append(pd.read_csv(RAW_DATA_DIR / 'twitter-2016test-CE.txt', sep='\t', header=None, names=column_names))
    datasets.append(pd.read_csv(RAW_DATA_DIR / 'twitter-2016train-CE.txt', sep='\t', header=None, names=column_names))

    # Concatenate the datasets
    df = pd.concat(datasets, axis=0, ignore_index=True)
    print(df.head())

    # Save the formatted data
    df.to_parquet(DATA_DIR / 'twitter-2016.parquet', index=False)
