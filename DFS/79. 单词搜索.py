"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

整体思路
使用深度优先搜索（DFS）和回溯的思想实现。关于判断元素是否使用过，我用了一个二维数组 mark 对使用过的元素做标记。

外层：遍历
首先遍历 board 的所有元素，先找到和 word 第一个字母相同的元素，然后进入递归流程。假设这个元素的坐标为 (i, j)，进入递归流程前，先记得把该元素打上使用过的标记：


mark[i][j] = 1
内层：递归
好了，打完标记了，现在我们进入了递归流程。递归流程主要做了这么几件事：

从 (i, j) 出发，朝它的上下左右试探，看看它周边的这四个元素是否能匹配 word 的下一个字母
如果匹配到了：带着该元素继续进入下一个递归
如果都匹配不到：返回 False
当 word 的所有字母都完成匹配后，整个流程返回 True
几个注意点
递归时元素的坐标是否超过边界
回溯标记 mark[i][j] = 0以及 return 的时机

解题思路
观摩精选题解的大佬思路有所收获，总的来讲这题就两个难点：
(1)通过何种形式回溯，一开始我的想法是把word转成一个列表并倒序，然后逐个弹出末尾值维护这个列表，通过回溯算法维护这个列表，但是越写越乱，这里其实可以通过一个与board相同大小的标记矩阵来进行回溯，同时标记矩阵还可以规避重复利用相同位置的元素的情况；
(2)设置位移数组，这个其实也不是太难想到，关键还是(1)

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):  # 0-index
                    return True
        return False

    def helper(self, board, i, j, word, wordIndex):
        if wordIndex == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
            return False

        board[i][j] = "#"

        found = self.helper(board, i + 1, j, word, wordIndex + 1) \
                or self.helper(board, i, j + 1, word, wordIndex + 1) \
                or self.helper(board, i, j - 1, word, wordIndex + 1) \
                or self.helper(board, i - 1, j, word, wordIndex + 1)
        board[i][j] = word[wordIndex]
        return found



class Solution:
    orientation = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    def exist(self, board, word):
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        mark = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.DFS(board, word, 0, i, j, mark, m, n):
                    return True
        return False

    def DFS(self, board, word, index, start1, start2, mark, m, n):
        if index == len(word)-1:
            return word[index] == board[start1][start2]
        if board[start1][start2] == word[index]:
            mark[start1][start2] = True
            for k in self.orientation:
                start_x = start1+k[0]
                start_y = start2+k[1]
                if 0 <= start_x < m and 0 <= start_y < n:
                    if not mark[start_x][start_y] and self.DFS(board, word, index+1, start_x, start_y, mark, m, n):
                        return True
            mark[start1][start2] = False
        return False
