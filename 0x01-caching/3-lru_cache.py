#!/usr/bin/python3
""" 4. LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a Least Recently Used caching system """

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
            least_recent = self.order.pop(0)
            del self.cache_data[least_recent]
            print(f"DISCARD: {least_recent}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
