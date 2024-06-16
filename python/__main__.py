#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import configparser
import os
from src.read import Read
from src.extract import Extract
from terminaltexteffects.effects import effect_decrypt


@click.command()
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    custom_separator = config.get('Parameter', 'custom_separator')
    db_name = config.get('Database', 'db_name')
    path = config.get('Folder', 'path')

    read = None
    if click.confirm(
        'Do you want remove taxpayers collection?', default=True, abort=False
    ):
        print('Setting up collection deletion')
        read = Read(db_name, custom_separator, drop=True)
    else:
        print('Setting up collection non deletion')
        read = Read(db_name, custom_separator, drop=False)

    print('Starting reading data')
    read.read_data(path)

    if click.confirm('Do you want remove duplicates?', default=True, abort=False):
        print('Starting removing duplicates')
        read.remove_duplicates()

        if click.confirm('Do you want create index?', default=True, abort=False):
            print('Starting creating index')
            read.create_index()

    if click.confirm(
        'Do you want extract and insert into persons?', default=True, abort=False
    ):
        extract = Extract(db_name)
        print('Starting extracting data for insert into persons')
        extract.extract_and_insert()
        extract.create_index()


if __name__ == '__main__':
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    effect = effect_decrypt.Decrypt('Read SRI catalogue and insert into MongoDB')
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    main()
