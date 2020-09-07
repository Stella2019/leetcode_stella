"""
递归
题目要求中序遍历。这里给递归解法和遍历解法，要背会哦～

递归方法比较简单，直接按照左子树->该节点->右子树的顺序遍历即可。

如果有不明白的，直接看官方解答，有图文：https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def inorder(root):
            if root == None:
                return None
            if root.left != None:
                inorder(root.left)
            answer.append(root.val)
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return answer


"""
迭代
迭代解法需要用到栈，这个方法确实比递归难得多了。

我们先把节点所有的左节点放入栈中，然后开始出栈，每次出栈都把栈中的元素放入到结果中，并且把这个结果的右孩子放入栈中。

因此，这里的遍历顺序先沿着最左方向到达最左下角的孩子，然后每次弹出来一个节点，把该节点的值放入结果中，并开始处理该节点的右子树。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        answer = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return answer
            root = stack.pop()
            answer.append(root.val)
            root = root.right
