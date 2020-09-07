"""
1339. 分裂二叉树的最大乘积
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。
"""

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            res = dfs(root.left) + dfs(root.right) + root.val
            sums_list.append(res)
            return res

        sums_list = []
        total = dfs(root)
        sums_list.sort()
        loc = bisect.bisect_left(sums_list, total >> 1)
        l, r = sums_list[loc - 1], sums_list[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)
