"""
题目大意
有一个密码锁，上面有四个旋钮，每个旋钮上面是0——9各个连续的数字，然后这个旋钮的0和9是连接着的。下面要去求从起始开始的"0000"扭到target，最少需要多少步。注意，其中有些deadends，表示如果扭到这里之后锁就坏掉。

解题方法
典型的搜索题目，可以抽象为一个无向图，在这个图中搜索target。因为求最少需要多少步，所以使用的方法是bfs。

方法很暴力了，属于模板。BFS需要一个队列和visited集合，通过step保存寻找了多少步，使用size保存当前有多少步可以搜素。使用j来遍历4个旋钮，使用k= -1, 1来表示能正向搜索和反向搜索。

这个BFS很暴力，也能过，当做模板背下来不错。
"""
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if (target in deadset) or ("0000" in deadset): return -1
        que = collections.deque()
        que.append("0000")
        visited = set(["0000"])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for j in range(4):
                    for k in range(-1, 2, 2):
                        newPoint = [i for i in point]
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))
                        newPoint = "".join(newPoint)
                        if newPoint == target:
                            return step
                        if (newPoint in deadset) or (newPoint in visited):
                            continue
                        que.append(newPoint)
                        visited.add(newPoint)
        return -1
"""二刷，使用的也是BFS，但是没有使用for循环使得代码比较罗素。"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        que = collections.deque()
        que.append("0000")
        visited = set(deadends)
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == target:
                    return step
                nodelist = map(int, list(node))
                que.append("".join(map(str, [(nodelist[0] + 1 + 10) % 10, nodelist[1], nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [(nodelist[0] - 1 + 10) % 10, nodelist[1], nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], (nodelist[1] + 1 + 10) % 10, nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], (nodelist[1] - 1 + 10) % 10, nodelist[2], nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], (nodelist[2] + 1 + 10) % 10, nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], (nodelist[2] - 1 + 10) % 10, nodelist[3]])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], nodelist[2], (nodelist[3] + 1 + 10) % 10])))
                que.append("".join(map(str, [nodelist[0], nodelist[1], nodelist[2], (nodelist[3] - 1 + 10) % 10])))
            step += 1
        return -1
