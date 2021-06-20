#exploration based on https://blog.datasyndrome.com/python-and-parquet-performance-e71da65269ce

#Parquet format is optimized in three main ways: columnar storage, columnar compression and data partitioning.


#https://arrow.apache.org/docs/python/parquet.html
import pyarrow.parquet as pq

import numpy as np

import pandas as pd

import pyarrow as pa

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))


table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')