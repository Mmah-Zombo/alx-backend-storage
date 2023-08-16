#!/usr/bin/env python3
"""
Main file
"""


import redis
import uuid


class Cache:
    """a cache class in redis py"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """stores the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
