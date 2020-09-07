#BFS/DFS


"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

题目大意
找出距离二叉树上某个节点距离为target的所有节点。注意不仅要向下寻找，还可以通过父亲节点反向寻找。

解题方法
第一眼看到这个题就感觉到这个题是个BFS问题，因为是满足条件的搜索问题，而且同时向不同方向寻找，找到之后提前终止。很像刚做过的，752. Open the Lock 。

所以这个题的做法就是通过DFS建立一个邻接矩阵，然后在这个邻接矩阵上使用BFS。这个BFS的做法和752题基本雷同，只是终止条件不同。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#A recursive dfs funciton connect help to build up a map conn.
#The key of map is node's val and the value of map is node's connected nodes' vals.
#Then we do N times bfs search loop to find all nodes of distance K
import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        conn = collections.defaultdict(list)
        def connect(parent, child):
        # both parent and child are not empty
            if parent and child:
            # building an undirected graph representation, assign the
            # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
        # in-order traversal
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
    # the initial parent node of the root is None
        connect(None, root)
    # start the breadth-first search from the target, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
    # all nodes at (k-1)th level must also be K steps away from the target node
        for i in range(K):
        # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
        # add all the values in bfs into seen
            seen |= set(bfs)
        return bfs


#下面的这个写法是在一个邻接矩阵中找出离某一个点距离是k的点
# BFS
"""bfs = [target.val]
visited = set([target.val])
for k in range(K):
    bfs = [y for x in bfs for y in conn[x] if y not in visited]
    visited |= set(bfs)
return bfs
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # DFS
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        # BFS
        bfs = [target.val]
        visited = set([target.val])
        for k in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in visited]
            visited |= set(bfs)
        return bfs
