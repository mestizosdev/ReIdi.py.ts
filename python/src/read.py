#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pymongo import MongoClient

file_path = '../csv/SRI_RUC_Galapagos.csv'
custom_separator = '|'

client = MongoClient('mongodb://localhost:27017/')
db = client['ecuador']
collection = db['entities']


def read_file():
    df = pd.read_csv(file_path, sep=custom_separator, encoding='latin')
    #  print(df.head())
    data = df.to_dict(orient='records')
    collection.insert_many(data)
