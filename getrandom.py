import random

class RandomizedSet(object):

    def __init__(self):
        # list to store elements
        self.nums = []
        # hashmap to store value -> index in the list
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        # get index of element to remove
        idx = self.pos[val]
        last = self.nums[-1]

        # move last element to the 'idx' position
        self.nums[idx] = last
        self.pos[last] = idx

        # remove last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
