"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.


给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

 

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

从一个节点出发，使用 DFS 对一个图进行遍历时，能够遍历到的节点都是从初始节点可达的，DFS 常用来求解这种 可达性 问题。
在程序实现 DFS 时需要考虑以下问题: 栈:用栈来保存当前节点信息，当遍历新节点返回时能够继续遍历当前节点。可以使用递归栈。
标记:和 BFS 一样同样需要对已经遍历过的节点进行标记。
对于这道题，我们遍历二维数组的时候，遇到1了，肯定是要检查上下左右是否依然是1(同时注意不要超出边界)， 如果检查出某一边是1，则还要进一步继续检查它的上下左右是否是1，这说明我们要通过递归来做，遍历时每遇到一 个1，就放到递归中去检测并计算岛屿面积。
此外，为了避免循环计算重复的区域，我们要改变已经计算过的岛屿的位置的值，可以从1改成0。 这种递归方式其实就是一种DFS，遇到一个1，则找遍其四周及四周的四周等等，来计算一个岛屿面积，同时改变找
过的1的值，避免重复计算。
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.r, self.c, max_area = len(grid), len(grid[0]), 0
        for i in range(self.r):
            for j in range(self.c):
                max_area = max(max_area, self.dfs(grid, i, j))
        return max_area

    def dfs(self, grid: List[List[int]], n: int, m: int) -> int:
        if n < 0 or n >= self.r or m < 0 or m >= self.c or grid[n][m] == 0:
            return 0
        area, grid[n][m] = 1, 0
        area += self.dfs(grid, n - 1, m)
        area += self.dfs(grid, n + 1, m)
        area += self.dfs(grid, n, m + 1)
        area += self.dfs(grid, n, m - 1)
        return area

#recursion
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        def dfs(i, j):
            if 0<=i<R and 0<=j<C and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            else:
                return 0
        result = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    result = max(result, dfs(r, c))
        return result

#stack iteration dfs
class Soultion:
  def maxAreaOfIsland(self, grid):
    def valid(ii, jj, c1, c2):
      return 0<=c1+ii<R and 0<=c2+jj<C and grid[c1+ii][c2+jj] == 1
    if not grid: return 0
    R,C = len(grid), len(grid[0])
    direct = {(0,1), (0, -1),(1, 0),(-1, 0)}
    count = 0
    max_area = 0
    for r in range(R):
      for c in range(C):
        if grid[r][c] == 1:
          stack = []
          stack.append((r, c))
          area = 1
          grid[r][c]= 0 #seen
          while stack:
            c1, c2 = stack.pop()
            for ii, jj in direc:
              if valid(ii, jj, c1, c2):
                stack.append((c1 + ii, c2 + jj))
                area += 1
                grid[c1 + ii][c2 + jj] = 0 #seen
          count += 1
          if area > max_area:
            max_area = area
    return max_area