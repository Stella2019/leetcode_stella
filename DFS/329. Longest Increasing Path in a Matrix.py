"""
题目大意
求二维矩阵中最长的递增路径。

解题方法
和417. Pacific Atlantic Water Flow非常类似，直接DFS求解。一般来说DFS需要有固定的起点，但是对于这个题，二维矩阵中的每个位置都算作起点。

把每个位置都当做起点，然后去做个dfs，看最长路径是多少。然后再找出全局的最长路径。使用cache保存已经访问过的位置，这样能节省了很多搜索的过程，然后有个continue是为了剪枝。因为这个做法比较暴力，就没有什么好讲的了。

最坏情况下的时间复杂度是O((MN)^2)，空间复杂度是O(MN)。
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        cache = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, cache, m, n, i, j)
                res = max(res, path)
        return res

    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 1
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            path = 1 + self.dfs(matrix, cache, m, n, x, y)
            res = max(path, res)
        cache[i][j] = res
        return cache[i][j]

 
