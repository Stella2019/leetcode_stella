"""
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

解题方法
题意是要求我们，找出一个最小的时间t，在t时刻时所有位置的水面的高度都是t，这时能从左上角的位置到达右下角。

既然指定了开始和结束的位置，可以直接使用DFS或者BFS进行搜索。这个题需要做的就是我们在每个时间t的时候，判断我们能否找到一个有效的路径，如果使用dfs搜索的话，需要判断两个格子的水位相等才行，因为只有海拔相等的情况下，才能保证游过去。因为每个格子自身都有个海拔，所以判断当前高度的方法其实是时刻与自身海拔的最大值。

为了加快搜索，使用了二分查找，题目已经说了所有的数字0～N*N-1之间，每次做二分的时候都要完整的做一次DFS，还好题目规模不大。

时间复杂度是O(N2*log(N))，空间复杂度是O(N2)。
"""


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        left, right = 0, n * n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if self.dfs([[False] * n for _ in range(n)], grid, mid, n, 0, 0):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def dfs(self, visited, grid, mid, n, i, j):
        visited[i][j] = True
        if i == n - 1 and j == n - 1:
            return True
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or max(mid, grid[i][j]) != max(mid, grid[x][y]):
                continue
            if self.dfs(visited, grid, mid, n, x, y):
                return True
        return False

"""
第二种解法是使用优先级队列。

这个思路是，从左上角通往右下角的路径中，瓶颈是哪个呢？肯定是那个必经的道路上有个比较高的。所以，我们只要在做BFS时候，优先走比较矮的路，同时把最高的那个保存下来，就是结果
"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited, pq = set((0, 0)), [(grid[0][0], 0, 0)]
        res = 0
        while pq:
            T, i, j = heapq.heappop(pq)
            res = max(res, T)
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            if i == j == n - 1:
                break
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                    continue
                heapq.heappush(pq, (grid[x][y], x, y))
                visited.add((x, y))
        return res

