#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python
    :param mongo_collection: Collection to use in mongodb
    :param kwargs: Any value to insert into mongodb
    :return: Returns the new _id assign to the document
    """
    new_insert = mongo_collection.insert_one(kwargs)
    _id = new_insert.inserted_id
    return _id
