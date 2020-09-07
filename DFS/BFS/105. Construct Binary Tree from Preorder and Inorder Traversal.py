"""Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
import self as self


class TreeNode:
    def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder[1: inorderIndex+1], inorder[: inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex + 1:], inorder[ inorderIndex+1:])

        return root