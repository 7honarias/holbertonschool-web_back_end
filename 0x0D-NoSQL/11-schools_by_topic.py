#!/usr/bin/env python3
""" Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """
    Get list of school having a specific topic
    :param mongo_collection: Collection to use in mongodb
    :param topic: Topic to search
    """
    return mongo_collection.find({'topics': {'$eq': topic}})
