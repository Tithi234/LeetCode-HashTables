class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
         # Using XOR operation
         result = 0
         for num in nums:
             result ^= num
         return result
