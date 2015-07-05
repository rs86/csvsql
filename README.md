# csvsql
Query CSV files using SQL.

## How to use it

    cat <csv-file> | python csvsqp.py <SQL>

## How it works

It just creates a SQLite3 in-memory database, loads data from the CSV file using Pandas and then queries it.

The table is loaded into the database as table "t".

## What we should do next

The script uses Pandas to load data into the SQLite3 instance using DataFrame.to_sql and queries the data also using DataFrame.read_sql. 

We need a lighter way to do it.
