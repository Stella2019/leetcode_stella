#bfs

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q, res = [(root, 1)], []
        if not root:
            return res

        while q != []:
            node, level = q.pop(0)
            if node.left != None:
                q.append((node.left, level + 1))
            if node.right != None:
                q.append((node.right, level + 1))
            if level == len(res):
                res[level - 1].append(node.val)
            else:
                res.append([node.val])

        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        return res