#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pymongo import MongoClient


class Read:
    def __init__(self, database: str, separator: str, drop=False):
        self.__database = database
        self.__separator = separator
        self.__drop_collection = drop
        self.file_path = '../csv/SRI_RUC_Galapagos.csv'
        client = MongoClient(self.__database)
        db = client['ecuador']
        self.collection_entities = db['entities']

    def read_file(self):
        df = pd.read_csv(
            self.file_path, dtype=str, sep=self.__separator, encoding='latin'
        )

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
