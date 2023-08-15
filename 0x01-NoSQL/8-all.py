#!/usr/bin/env python3
"""mongo this"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    docs = list(mongo_collection.find())
