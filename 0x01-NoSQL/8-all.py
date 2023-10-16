#!/usr/binenv python3
''' list of docs in collection '''


def list_all(mongo_collection):
    ''' returns list of all documents in collection '''
    return [doc for doc in mongo_collection.find()]
