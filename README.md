# csvsql

Query CSV files using SQL.

## How to use it

csvfile -f filename -s sql

## How it works

The script loads CSV files into a SQLite3 database and queries them. It saves the database do disk, so the CSV files are actually cached. It uses Adler32 checksums to check if the data cached on the SQLite DB is the same as in disk.

The CSV will have its filename as table name, so for instance you can query iris.csv as table iris.
