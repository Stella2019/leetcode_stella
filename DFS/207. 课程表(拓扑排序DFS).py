"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
通过次数71,973提交次数133,117


题目分析

这道题是一道拓扑排序的题目，但是我们并不用完成拓扑排序，只需要判断图中是否存在环即可。


拓扑排序用 BFS 和 DFS 两种都可以实现，BFS 的实现复杂度较高，因此此处我们选用 DFS 来实现。

对于使用 DFS 实现，我们每次找到一个新的点，判断从这个点出发是否有

具体做法是使用一个 visited 数组，当 visited 值为 0, 说明还没判断这个点；当 visited 值为 1,
说明当前的循环正在判断这个点；当 visitedl 值为 2, 说明已经判断过这个点，含义是从这个点往后的所有路径都没有环
，认为这个点是安全的

那么，我们对每个点出发都做这个判断，检查这个点出发的所有路径上是否有环，
如果判断过程中找到了当前的正在判断的路径，说明有环；找到了已经判断正常的点，说明往后都不可能存在环，所以认为当前的节点也是安全的。如果当前点是未知状态，那么先把当前点标记成正在访状态，然后找后续的节点，直到找到安全的节点为止。最后如果到达了无路可走的状态，说明当前节点是安全的。
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #首先对传递过来的连接关系进行处理
        graphic = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graphic[pre[0]].append(pre[1])
        #申请一个标记数组，其中为表示未访问，1 表示正在访问，2 表示访问完成
        visited = [0] * numCourses
        for i in range(numCourses):
            #判断是否有环
            if self.exist_cycle(visited, graphic, i):
                return False
        return True

    def exist_cycle(self, visited, graphic, cur_node):
        #如果当前访问到的节点状态是 1, 也就是表示正在被访问，有环
        if visited[cur_node] == 1:
            return True
        #当前访问到的节点状态是 2, 表示访问完成
        if visited[cur_node] == 2:
            return False
        #否则表示是一个未访问过的节点，我们先把状态置为 1
        visited[cur_node] = 1
        for next_node in graphic[cur_node]:
            #深度遍历其指向子节点，并且从每个子节点寻找子节点后面是否存在环
            if self.exist_cycle(visited, graphic, next_node):
                return True
            #节点访问完把状态置为访问结
            visited[cur_node] = 2
            return False