#!/usr/bin/env python
import pandas as pd
import ctypes
import sqlite3
import sys
import zlib
import argparse
import csv
import os

# Always pass the database as the first argument.

def signed_checksum(data):
    return ctypes.c_uint32(zlib.adler32(data)).value

def open_connection():
    conn = sqlite3.connect('csvsql.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS checksums (filename TEXT, checksum INTEGER)')
    conn.commit()
    return conn

def needs_update(db, filename, checksum):
    cur = db.cursor()
    cur.execute('SELECT checksum FROM checksums WHERE filename=?', [filename])
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute('INSERT INTO checksums VALUES (?, ?)', [filename, checksum])
        return True
    if rows[0][0] == checksum:
        return False
    return True

def update_db(db, filename):
    with open(filename, 'rb') as input_file:
        data = input_file.read()
        checksum = signed_checksum(filename)
        if needs_update(db, filename, checksum):
            df = pd.read_csv(filename)
            df.to_sql(filename[0:-4], db)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='input_filename', action='store', required=True)
    parser.add_argument('-s', dest='sql_command', action='store', required=True)
    options = parser.parse_args(argv)

    if not os.path.isfile(options.input_filename):
        sys.stderr.write('File {0} does not exist.'.format(options.input_filename))
        return

    conn = open_connection()
    update_db(conn, options.input_filename)
    cur = conn.cursor()
    cur.execute(options.sql_command)
    for row in cur:
        print row

main(sys.argv[1:])
