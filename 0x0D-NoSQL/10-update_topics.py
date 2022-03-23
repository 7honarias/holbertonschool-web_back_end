#!/usr/bin/env python3
""" Change school topics """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    :param mongo_collection: Collection to use in mongodb
    :param name: School name to update
    :param topics: list of topics approached in the school
    """
    filter = {'name': name}
    new_topics = {"$set": {'topics': topics}}
    mongo_collection.update_many(filter, new_topics)
