#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pymongo import MongoClient

file_path = '../csv/SRI_RUC_Galapagos.csv'
custom_separator = '|'

client = MongoClient('mongodb://localhost:27017/')
db = client['ecuador']
collection_entities = db['entities']


def read_file():
    df = pd.read_csv(file_path, dtype=str, sep=custom_separator, encoding='latin')

    print(df.dtypes)
    print(df.head())
    selection = df[['NUMERO_RUC', 'RAZON_SOCIAL']]
    selection.rename(columns={'NUMERO_RUC': 'identification', 'RAZON_SOCIAL': 'name'}, inplace=True)
    print(selection)

    data = selection.to_dict(orient='records')
    collection_entities.drop()
    collection_entities.insert_many(data)
