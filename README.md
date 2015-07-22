# csvsql

Query CSV files using SQL.

## How to use it

csvfile -f <csv file name> -s <sql query>

## How it works

The script loads CSV files into a SQLite3 database and queries them. It saves the database do disk, so the CSV files are actually cached. It uses Adler32 checksums to check if the data cached on the SQLite DB is the same as in disk.
