#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient


class Extract:
    def __init__(self, database: str):
        self.__database = database
        client = MongoClient(self.__database)
        db = client['ecuador']
        self.collection_persons = db['persons']
        self.collection_taxpayers = db['taxpayers']

    def extract_and_insert(self):
        pipeline = [
            {'$match': {'type': 'PERSONAS NATURALES'}},
            {
                '$project': {
                    '_id': 0,
                    'identification': {'$substr': ['$identification', 0, 10]},
                    'name': 1,
                    'province': 1,
                    'canton': 1,
                    'parish': 1,
                    'created_at': 1,
                }
            },
        ]
        results = self.collection_taxpayers.aggregate(pipeline)

        results_list = list(results)

        try:
            self.collection_persons.drop()
            self.collection_persons.insert_many(results_list)
        except Exception as e:
            print('Error to insert: ', e)

    def create_index(self):
        self.__remove_duplicates()
        self.collection_persons.create_index(
            [('identification', 'text')], name='identification_text', unique=True
        )

        print('Finished creating indexes in persons collection')

    def __drop_index(self):
        self.collection_persons.drop_index([('identification', 'text')])
        print('Finished dropping indexes in persons collection')

    def __remove_duplicates(self):
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

        results = self.collection_persons.aggregate(pipeline)
        results_list = list(results)

        for result in results_list:
            # print('Duplicated: ')
            # print('Identification: ', result['_id']['identification'])
            # print('Count:', result['count'])
            i = 1
            for uniqueId in result['uniqueIds']:
                if i > 1:
                    self.collection_persons.delete_one({'_id': uniqueId})
                    #  print(f'Deleted: {uniqueId} -> {result['_id']['identification']}')
                i += 1

        print('Finished removing duplicates in persons collection')
