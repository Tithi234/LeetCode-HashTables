from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Step 1: Count frequency of each number
        count = Counter(nums)

        # Step 2: Bucket sort — create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: Collect from highest frequency downwards
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
