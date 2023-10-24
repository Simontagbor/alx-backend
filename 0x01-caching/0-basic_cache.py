#!/usr/bin/env python3
"""
Implements a subclass of BasicCaching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A subclass of BasicCaching that implements a basic caching system.

    Attributes:
                None
    Methods:
            put(key, item) - updates the instances's cache_data with
            the key specified returns none if none of the args are specified

            get(key) - returns the value in the cache data and none if key
            is not found or not specified
    """

    def put(self, key, item):
        """Adds an item to cache_data

        Args:
            key(str) - key -> item
            item(any) - item to be inserted

        Returns:
                None
        """
        if key is not None and item is not None:
            self.cache_data.update({f"{key}": item})

    def get(self, key):
        """
        Retrieves an item from cache with a specified key

        Args:
            key(str) - key for retrieving the associated key

        Returns:
            value(any) - stored item in the cache_data
        """
        if key is not None or key in self.cache_data:
            return self.cache_data.get(key)
        return None
