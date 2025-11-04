class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import Counter

        # Step 1: Count all possible sums of nums1 and nums2
        sum12 = Counter(a + b for a in nums1 for b in nums2)

        # Step 2: For each possible sum of nums3 and nums4, check if its negative is in sum12
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum12:
                    count += sum12[target]

        return count
