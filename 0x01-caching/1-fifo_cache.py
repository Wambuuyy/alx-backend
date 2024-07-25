#!/usr/bin/python3
""" BasicCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """this one has a limit"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """retrieve item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
