#!/usr/bin/env python
# -*- coding: utf-8 -*-
import src.read as read


def main():
    print('Read SRI Catalogue and insert into MongoDB')
    read.read_file()


if __name__ == '__main__':
    main()
