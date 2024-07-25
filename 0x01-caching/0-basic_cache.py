#!/usr/bin/env python3
"""
caching system with no limits
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """use dict from parent"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        return self.cache_data.get(key, None)
