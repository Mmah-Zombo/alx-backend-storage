#!/usr/bin/env python3
"""
Main file
"""


import redis
import uuid
from typing import Union


class Cache:
    """a cache class in redis py"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, float]) -> str:
        """stores the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
