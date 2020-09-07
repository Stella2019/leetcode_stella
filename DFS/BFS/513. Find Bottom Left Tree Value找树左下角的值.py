# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root: return None
        q = deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if i == 0:
                    leftmost = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return leftmost

#我们想要找到左下角的值，可以将层序遍历本来同一层从左到右改成从右到左遍历即可。 答案
 # Definition for a binary tree node.
 # class TreeNode:
    # def __init__(self, x):
    # self.val = x
    # self.left = None
    # self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        while q:
            root = q.pop(0)
            if root.right:
                q.append(root.right)
            if root.left:
                q.append(root.left)
        return root.val