#!/usr/bin/env python
import sqlite3
import pandas as pd
import sys

conn = sqlite3.connect(':memory:')

df = pd.read_csv(sys.stdin)
df.columns = df.columns.map(lambda x: x.replace(" ", ""))
df.to_sql('t', conn)

df = pd.read_sql(sys.argv[1], conn)

print df
