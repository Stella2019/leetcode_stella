"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

题目分析
平衡二叉树 (空树或者左右两个孩子高度差不超过1) 在涉及到二叉树的题目时，递归函数非常好用 1.左子树是否平衡
2.右子树是否平衡
3.左子树的高度 4.右子树的高度
整个递归过程按照同样的结构得到子树的信息(左子树和右子树分别是否平衡，以及它们的高度)，整合子树的信息 ( )，加工出返回的信息(应该返回左右子树中，高度较大的那一个high+1)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(root):
            if root is None:
                return 0
            left_height, right_height = get_height(root.left), get_height(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return (get_height(root) >= 0)


# Definition for a binary tree node.
 # class TreeNode:
    # def __init__(self, x):
    # self.val = x
    # self.left = None
    # self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if abs(left_height-right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def getHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1
