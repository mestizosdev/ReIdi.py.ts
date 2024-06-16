#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
from src.read import Read


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    custom_separator = config.get('Parameter', 'custom_separator')
    db_name = config.get('Database', 'db_name')

    print('Read SRI catalogue and insert into MongoDB')

    read = Read(db_name, custom_separator, drop=True)
    read.read_file()


if __name__ == '__main__':
    main()
