# csvsql
Query CSV files using SQL.

## How to use it

    cat <csv-file> | python csvsqp.py <SQL>

## How it works

It just creates a SQLite3 in-memory database, loads data from the CSV file using Pandas and then queries it.

The table is loaded into the database as table "t".
