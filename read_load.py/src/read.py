#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd
from pymongo import MongoClient


class Read:
    def __init__(self, database: str, separator: str, drop=False):
        self.__database = database
        self.__separator = separator
        self.__drop_collection = drop
        client = MongoClient(self.__database)
        db = client['ecuador']
        self.collection = db['taxpayers']

    def read_data(self, path: str):
        if self.__drop_collection:
            self.collection.drop()
            print('Droped collection taxpayers')

        dir_list = os.listdir(path)

        for file in dir_list:
            file_path = path + file
            if file.endswith('.csv'):
                print(f'Read file: {file_path}')
                self.__read_files(file_path)

    def __read_files(self, file_path: str):
        try:
            df = pd.read_csv(file_path, dtype=str, sep=self.__separator, encoding='latin')

            print(df.dtypes)
            print(df.head())
            selection = df[
                [
                    'NUMERO_RUC',
                    'RAZON_SOCIAL',
                    'NOMBRE_FANTASIA_COMERCIAL',
                    'CLASE_CONTRIBUYENTE',
                    'TIPO_CONTRIBUYENTE',
                    'DESCRIPCION_PROVINCIA_EST',
                    'DESCRIPCION_CANTON_EST',
                    'DESCRIPCION_PARROQUIA_EST',
                    'ACTIVIDAD_ECONOMICA',
                    'OBLIGADO',
                    'CODIGO_CIIU',
                    'ESTADO_CONTRIBUYENTE',
                ]
            ]

            selection_copy = selection.copy()
            selection_copy.rename(
                columns={
                    'NUMERO_RUC': 'identification',
                    'RAZON_SOCIAL': 'name',
                    'NOMBRE_FANTASIA_COMERCIAL': 'trade_name',
                    'CLASE_CONTRIBUYENTE': 'category',
                    'TIPO_CONTRIBUYENTE': 'type',
                    'DESCRIPCION_PROVINCIA_EST': 'province',
                    'DESCRIPCION_CANTON_EST': 'canton',
                    'DESCRIPCION_PARROQUIA_EST': 'parish',
                    'OBLIGADO': 'mandatory_accounting',
                    'ACTIVIDAD_ECONOMICA': 'economic_activity',
                    'CODIGO_CIIU': 'code_ciiu',
                    'ESTADO_CONTRIBUYENTE': 'status',
                },
                inplace=True,
            )

            print(selection_copy)
            data = selection_copy.to_dict(orient='records')
            self.__load_into_database(data)
        except Exception as e:
            print('Error to read file: ', file_path, e)

    def __load_into_database(self, data: dict):
        self.collection.insert_many(data)
        print('Finished inserting into taxpayers collection')

    def remove_duplicates(self):
        pipeline = [
            {
                '$group': {
                    '_id': {'identification': '$identification'},
                    'uniqueIds': {'$addToSet': '$_id'},
                    'count': {'$sum': 1},
                }
            },
            {'$match': {'count': {'$gt': 1}}},
        ]

        results = self.collection.aggregate(pipeline)
        results_list = list(results)

        for result in results_list:
            # print('Duplicated: ')
            # print('Identification: ', result['_id']['identification'])
            # print('Count:', result['count'])
            i = 1
            for uniqueId in result['uniqueIds']:
                if i > 1:
                    self.collection.delete_one({'_id': uniqueId})
                    #  print(f'Deleted: {uniqueId} -> {result['_id']['identification']}')
                i += 1

        print('Finished removing duplicates in taxpayers collection')

    def create_index(self):
        self.collection.create_index(
            [('identification', 'text')], name='identification_text', unique=True
        )

        print('Finished creating indexes in taxpayers collection')
