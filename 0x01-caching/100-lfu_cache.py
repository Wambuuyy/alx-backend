#!/usr/bin/python3
""" 100-lfu_cache module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.freq = {}
        self.usage = {}
        self.time = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and increase frequency
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            # Add the item to the cache and set frequency to 1
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                min_freq = min(self.freq.values(), default=0)
                least_freq_keys = [k for k, v in self.freq.items()
                                   if v == min_freq]

                if len(least_freq_keys) == 1:
                    # Only one item with minimum frequency
                    lfu_key = least_freq_keys[0]
                else:
                    # Multiple items with the same frequency,
                    # find the least recently used
                    lfu_key = min(least_freq_keys, key=lambda k: self.usage[k])

                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                del self.usage[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add new item
            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage[key] = self.time
            self.time += 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Increase frequency and update usage timestamp
        self.freq[key] += 1
        self.usage[key] = self.time
        self.time += 1

        return self.cache_data[key]
