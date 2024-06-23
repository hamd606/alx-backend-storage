#!/usr/bin/env python3
"""
Change all school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school
     document using the name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
