#!/usr/bin/env python3
""" LIFO Caching module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a Last In First Out caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            last = self.order.pop()
            del self.cache_data[last]
            print(f"DISCARD: {last}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
