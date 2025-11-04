class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set = set(jewels)  # Convert jewels to a set for O(1) lookups
        count = 0

        for s in stones:
            if s in jewel_set:
                count += 1

        return count
