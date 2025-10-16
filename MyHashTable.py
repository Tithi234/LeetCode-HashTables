class MyHashSet(object):

    def __init__(self):
        self.size = 1000  # number of buckets
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        """Simple hash function"""
        return key % self.size

    def add(self, key):
        h = self.hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key):
        h = self.hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key):
        h = self.hash(key)
        return key in self.buckets[h]

