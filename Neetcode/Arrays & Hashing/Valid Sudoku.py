from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        squares = [[[] for _ in range(3)] for _ in range(3)]  # 3x3 grid of lists

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r // 3][c // 3]
                ):
                    return False
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                squares[r // 3][c // 3].append(board[r][c])

        return True

# Test Example 1
board1 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

# Test Example 2
board2 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

# Create an instance of Solution
sol = Solution()

# Test and print results
print("Example 1 is valid:", sol.isValidSudoku(board1))  # Expected output: True
print("Example 2 is valid:", sol.isValidSudoku(board2))  # Expected output: False
