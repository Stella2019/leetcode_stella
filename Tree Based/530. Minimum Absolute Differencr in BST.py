"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        self.InOrderTraversal(root, output)
        min_abs = float('inf')
        for i in range(1, len(output)):
            min_abs = min(min_abs, output[i] - output[i - 1])
        return min_abs

        self.InOrderTraversal(root, output)
    def InOrderTraversal(self, root, output):
        if root == None:
            return
        else:
            self.InOrderTraversal(root.left, output)
            output.append(root.val)
            self.InOrderTraversal(root.right, output)