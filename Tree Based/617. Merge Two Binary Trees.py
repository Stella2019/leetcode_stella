"""
把两个树重叠，重叠部分求和，不重叠部分是两个树不空的节点
"""
"""
题目大意
将两个二叉树进行merge操作。操作方式是把两个树进行重叠，如果重叠部分都有值，那么这个新节点是他们的值的和；如果重叠部分没有值，那么新的节点就是他们两个当中不为空的节点。

解题方法
递归
如果两个树都有节点的话就把两个相加，左右孩子为两者的左右孩子。

否则选不是空的节点当做子节点。

时间复杂度是O(N1+N2)，空间复杂度O(N)。N = t1 的 t2交集。
"""

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            newT = TreeNode(t1.val +  t2.val)
            newT.left = self.mergeTrees(t1.left, t2.left)
            newT.right = self.mergeTrees(t1.right, t2.right)
            return newT
        else:
            return t1 or t2
#也可以换一种写法，没有任何区别：

class Solution:
    def mergeTrees(self, t1, t2):
        if not t2:
            return t1
        if not t1:
            return t2
        newT = TreeNode(t1.val + t2.val)
        newT.left = self.mergeTrees(t1.left, t2.left)
        newT.right = self.mergeTrees(t1.right, t2.right)
        return newT
