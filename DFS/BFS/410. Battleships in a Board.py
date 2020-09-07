"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def is_valid(row, col):
            if row < 0 or col >= len(board) or col >= len(board[0]):
                return False
            else:
                return True

        def dfs(row, col):
            if not is_valid(row, col):
                return
            if board[row][col] == ".":
                return
            board[row][col] = "."
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)

        if not board:
            return

        battleship_count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    battleship_count += 1
                    dfs(row, col)

"""
遍历到'.'不用管
每遍历到一个'X'，战舰计数+1，并把这个战舰其余部分的'X'替换为'.'
遍历完成后直接return战舰计数
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X':
                    ans += 1
                    i = row
                    j = col
                    while j+1 < cols and board[i][j+1] == 'X':
                        board[i][j+1] = '.'
                        j += 1
                    while i+1 < rows and board[i+1][j] == 'X':
                        board[i+1][j] = '.'
                        i += 1
        return ans

"""
我们可以通过战舰的头来判断个数，当一个点上面或者左面试X说明它战舰中间部分，跳过即可！
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        res =  0
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".": continue
                if i > 0 and board[i - 1][j] == "X": continue
                if j > 0 and board[i][j - 1] == "X": continue
                res += 1
        return res
