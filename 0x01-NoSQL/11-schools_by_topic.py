#!/usr/bin/env python3
"""mongo this"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    query = {"topics": topic}
    result = list(mongo_collection.find(query,
                                        {"_id": 1, "name": 1, "topics": 1}))
    return result
