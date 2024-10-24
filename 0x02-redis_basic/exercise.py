#!/usr/bin/env python3
"""
Cache class implementation using Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize Redis connection and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        :param data: Data to store, can be of type str, bytes, int, or float.
        :return: The generated key as a string.
        """
        key = str(uuid.uuid4())  # Generate a random UUID string
        self._redis.set(key, data)  # Store the data in Redis
        return key

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decoded string.

        :param key: The key to retrieve from Redis.
        :return: The data decoded as a string, or None.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        :param key: The key to retrieve from Redis.
        :return: The data converted to an integer, or None.
        """
        return self.get(key, fn=int)
