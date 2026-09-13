class Solution:
    def dfs(self, r, c, visited, rows, cols, board):
        # If out of bounds, stop
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        # If it's an 'X', stop
        if board[r][c] == "X":
            return
        # If already marked as border-connected, stop
        if visited[r][c] == 1:
            return
        # Mark this 'O' as connected to the border
        visited[r][c] = 1
        # Recurse up, left, right, down
        self.dfs(r - 1, c, visited, rows, cols, board)
        self.dfs(r, c - 1, visited, rows, cols, board)
        self.dfs(r, c + 1, visited, rows, cols, board)
        self.dfs(r + 1, c, visited, rows, cols, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # 0 = unvisited, 1 = connected-to-border
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # 1. Check every cell on the border
        for r in range(rows):
            for c in range(cols):
                # Is this cell on the outer border?
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    # If it's an 'O' and not yet visited, run DFS
                    if board[r][c] == "O":
                        if visited[r][c] == 0:
                            self.dfs(r, c, visited, rows, cols, board)

        # 2. Flip all 'O's that were never marked
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"
