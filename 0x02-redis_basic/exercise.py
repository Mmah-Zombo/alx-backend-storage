#!/usr/bin/env python3
"""
Main file
"""


import redis
import uuid
from typing import Optional, Callable, Union


class Cache:
    """a cache class in redis py"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str,
            fn: Optional[Callable] = None,
            ) -> Union[str, bytes, int, float]:
        """gets the value"""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """gets the string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> str:
        """gets the string"""
        return self.get(key, fn=lambda d: int(d))
