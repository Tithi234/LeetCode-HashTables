class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype target: int
        :rtype: List[int]
        """
        seen = {} # stores num -> index mapping

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i 
