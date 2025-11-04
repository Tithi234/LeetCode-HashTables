# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        from collections import defaultdict

        serial_count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"

            # serialize subtree as a string
            serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            serial_count[serial] += 1

            # when a subtree is found the second time, add it to result
            if serial_count[serial] == 2:
                result.append(node)
            return serial

        serialize(root)
        return result
