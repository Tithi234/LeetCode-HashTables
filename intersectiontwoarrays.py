class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert both lists to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Find intersection
        return list(set1 & set2)
