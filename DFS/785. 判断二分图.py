"""
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

题目分析

对于本题来说，如果可以用两种颜色对图中的节点进行着色，并且保证相邻的节点颜色不同，那么这个图就是二分图

所以将本题转化成了一个着色题，同时用 dfs 进行遍历节点，即可完成对所有的节点的涂色与判断。
需要注意的是我们用-1表示未着色,0/1分别表示两种颜色。

"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
    #实际本题还是一个着色问题
    #初始化一个节点颜色1ist-1表示未涂色,/1分别表示两种颜色

    colors=[-1] *len (graph)
    for i in range (len (graph)):
        if colors [i] == -1 and not self.dfs (i, colors, graph):
            return False
    return True

    def dfs(self, cur_node, cur_color, colors, graph):
        if colors[cur_node] != -1
        #如果当前节点已涂色，则直接判断两次颜色是否相同并返回

        return colors[cur_node] == cur_color

#给节点涂色

        colors[cur_node] =cur_color
        for next_node in graph[cur_node]:

#1- cur color 表示与当前颜色相反的颜色
#深度遍历所有的节点

           if not self.dfs(next_node, 1 - cur_color, colors, graph):
               return False

            return True