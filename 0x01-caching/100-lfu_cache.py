#!/usr/bin/python3
""" 4. LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            least_frequent = min(self.usage_frequency.values())
            least_frequent_keys = [k for k, v in self.usage_frequency.items() if v == least_frequent]
            if len(least_frequent_keys) > 1:
                oldest_key = next(k for k in self.usage_order if k in least_frequent_keys)
            else:
                oldest_key = least_frequent_keys[0]
            del self.cache_data[oldest_key]
            del self.usage_frequency[oldest_key]
            self.usage_order.remove(oldest_key)
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.usage_frequency[key] = self.usage_frequency.get(key, 0) + 1
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
