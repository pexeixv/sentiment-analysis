import pandas as pd
import numpy as np

class stats:
    def get_stats(df):
        print('\n10 random sample:')
        print(df.sample(10))
        print('\n\nFirst 10 rows:')
        print(df.head(10))
        print('\n\nTotal columns:')
        print(df.columns)
        print('\n\nShape:')
        print(df.shape)
        print('\n\nOverall data:')
        print(df.info())
        print('\n\nData type;')
        print(df.dtypes)
        print('\n\nTotal number null rows:')
        print(np.sum(df.isnull().any(axis=1)))
        print('\n\nTotal target value:')
        print(df['category'].unique())