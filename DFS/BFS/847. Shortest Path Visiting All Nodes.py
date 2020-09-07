"""
需要找出某顶点到其他顶点的最短路径。出发顶点不是确定的，每个顶点有可能访问多次。
使用N位bit代表访问过的顶点的状态。如果到达了最终状态，那么现在步数就是所求。
这个题把所有的节点都放入了起始队列中，相当于每次都是所有的顶点向前走一步。
题目大意
在一个无向联通图中，可以从任意一点出发，找到最少需要多少步才能把所有的顶点遍历结束。每个边可以访问多次。

解题方法
方法一：BFS
话说看到这个题的第一感觉就是BFS，因为我们要找到遍历所有节点的最少步数，这个正是BFS擅长的。唯一不同的就是这个题允许从多个顶点出发，也就是说没有了固定的起点。那么需要对BFS稍微改变一点，即在初始化的时候，把所有顶点都放进队列之中，这样，每次把队列的元素pop出来一遍之后就是新的一轮循环，也就可以认为所有的节点都是同时向前迈进了一步。

这个题使用了一个的技巧，位运算。一般的BFS过程都是只保存访问过的节点即可，因为每个节点只可以使用一次，但是这个题的节点可以访问多次，那么就是说必须维护一个实时的访问了哪些节点的状态。按道理说，如果不使用位运算而是使用字典等方式保存访问过了的状态也可以，但是，看了给出的图的顶点个数只有12个，哪怕一个int都会有32个bit够用，所以可以直接使用和图中顶点数相等的位数来保存这个状态是否访问过。这个状态怎么理解？从每个顶点出发到达，所有访问过的节点是状态。也就是说这个状态是全局唯一的，每个顶点都有2 * N个状态表示它访问的其他节点。有2 ^ N个bit，每个位都代表对应的节点是否访问过。最终的状态是(1 << N) - 1，即全是1，表示所有节点都访问了。

这个visited是个二维数组，保存的是每个节点的所有状态，对于该题目的BFS，有可能有N * 2^Ｎ个状态，使用visited保存每个节点已经访问的状态，对应状态位置是0/1。

时间复杂度是O(N * (2^N))，空间复杂度是O(N * 2^Ｎ)。
"""
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        que = collections.deque()
        step = 0
        goal = (1 << N) - 1
        visited = [[0 for j in range(1 << N)] for i in range(N)]
        for i in range(N):
            que.append((i, 1 << i))
        while que:
            s = len(que)
            for i in range(s):
                node, state = que.popleft()
                if state == goal:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1
                for nextNode in graph[node]:
                    que.append((nextNode, state | (1 << nextNode)))
            step += 1
        return step
