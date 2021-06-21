#exploration based on https://arrow.apache.org/docs/python/parquet.html#reading-and-writing-single-files

#Parquet format is optimized in three main ways: columnar storage, columnar compression and data partitioning.


import pyarrow.parquet as pq

import numpy as np

import pandas as pd

import pyarrow as pa

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))


table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet') #creating a single parquet file

#reading it back in
table2 = pq.read_table('example.parquet')

df2 = table2.to_pandas()
print(type(df2))
print(df2.head())

#reading in a subset of columns
pq.read_table('example.parquet', columns=['one', 'three'])