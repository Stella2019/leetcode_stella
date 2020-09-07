"""

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

题目分析
对于网格中的元素                     ,从最上角的元素                     走到它的最短距离为:
][j] 因此，这题的思路是:首先计算出第一行从左到右的步
数。然后从第二行开始，采用动态规划的方法。
GRID[i][j] = min(grid[i - 1][i], grid[i][j - 1]) + grid [i][j]
事实上，我们只需要维护一个一维dp数组即可，这个数组代表走到对应行的每个位置的最短路径。当更新某位置dp[j] 的时候只需要上方路径信息dp[j](可以看作从上向下一遍一遍访问矩阵，更新dp，那么此时的dp[j]由于还未更新，所 以是上方位置的路径信息)和左侧路径信息dp[j-1]即可，所以dp数组可以不断的覆盖，而不需要维护二维dp数组。
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [0] * c
        for i in range(r):
            for j in range(c):
                if j == 0:
                    dp[j] = dp[j]
                elif i == 0:
                    dp[j] = dp[j - 1]
                else:
                    dp[j] = min(dp[j - 1], dp[j])
                dp[j] += grid[i][j]
        return dp[c - 1]