#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import configparser
import os
from src.read import Read
from src.extract import Extract


@click.command()
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    SEPARATOR = config.get('Parameter', 'SEPARATOR')
    DB = config.get('Database', 'DB')
    CSV_PATH = config.get('Folder', 'CSV_PATH')

    read = None
    if click.confirm(
        'Do you want remove taxpayers collection?', default=True, abort=False
    ):
        print('Setting up collection deletion')
        read = Read(DB, SEPARATOR, drop=True)
    else:
        print('Setting up collection non deletion')
        read = Read(DB, SEPARATOR, drop=False)

    print('Starting reading data')
    read.read_data(CSV_PATH)

    if click.confirm('Do you want remove duplicates?', default=True, abort=False):
        print('Starting removing duplicates')
        read.remove_duplicates()

        if click.confirm('Do you want create index?', default=True, abort=False):
            print('Starting creating index')
            read.create_index()

    if click.confirm(
        'Do you want extract and insert into persons?', default=True, abort=False
    ):
        extract = Extract(DB)
        print('Starting extracting data for insert into persons')
        extract.extract_and_insert()
        extract.create_index()


if __name__ == '__main__':
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    print('Read SRI catalogue and insert into MongoDB')
    main()
