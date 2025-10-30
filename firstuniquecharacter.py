class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Count frequency of each character
        from collections import Counter
        count = Counter(s)

        #Step 2: Find the first character with frequency
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        # Step 3: If no unique character, return -1
        return -1
