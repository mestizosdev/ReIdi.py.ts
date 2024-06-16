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
        self.collection_entities = db['entities']

    def read_data(self, path: str):
        dir_list = os.listdir(path)

        for file in dir_list:
            file_path = path + file
            print(f'Read file: {file_path}')
            self.__read_files(file_path)

    def __read_files(self, file_path: str):
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

    def __load_into_database(self, data: dict):
        if self.__drop_collection == True:
            self.collection_entities.drop()
            print('Droped collection entities')

        self.collection_entities.insert_many(data)
        print('Finished inserting into MongoDB')

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

        results = self.collection_entities.aggregate(pipeline)
        results_list = list(results)

        for result in results_list:
            # print('Duplicated: ')
            # print('Identification: ', result['_id']['identification'])
            # print('Count:', result['count'])
            i = 1
            for uniqueId in result['uniqueIds']:
                if i > 1:
                    self.collection_entities.delete_one({'_id': uniqueId})
                    print(f'Deleted: {uniqueId} -> {result['_id']['identification']}')
                i += 1
