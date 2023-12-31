#!/usr/bin/env python3
"""
Implements a subclass of BasicCaching class
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A subclass of BasicCaching that implements a FIFO caching system.

    Attributes:
                None
    Methods:
            put(key, item) - updates the instances's cache_data with
            the key specified returns none if none of the args are specified

            get(key) - returns the value in the cache data and none if key
            is not found or not specified
     """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns the item value to the key
        in the self.cache_data dictionary.
        """
        if key is not None and item is not None:
            self.cache_data.update({f"{key}": item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = list(self.cache_data)[0]
            self.cache_data.pop(first)
            print('DISCARD: {}'.format(first))

    def get(self, key):
        """
        Returns the value of the key in the
        self.cache_data dictionary.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
