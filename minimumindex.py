class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {name: i for i, name in enumerate(list1)} # Step 1
        min_sum = float('inf')
        res = []

        for j, name in enumerate(list2): # Step 2
            if name in index_map: # commomnn string
                total = j + index_map[name]

                if total < min_sum: # found smaller sum
                    min_sum = total
                    res = [name]
                elif total == min_sum: # same min sum
                    res.append(name)

        return res
