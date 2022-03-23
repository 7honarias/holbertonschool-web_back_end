#!/usr/bin/env python3
"""List all documents from mongo using Python"""


def list_all(mongo_collection):
    """List all documents from mongo using Python
    :param mongo_collection: Collection to use in mongodb
    :return: Return an empty list if no document in the collection or
    lists all documents of the collection."""

    documents = mongo_collection.find()
    if documents is not None:
        return list(documents)
    return []
