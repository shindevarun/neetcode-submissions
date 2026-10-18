class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))

            while q:
                row, col = q.popleft()
                
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]

                    if (
                        new_row < 0
                        or new_row >= len(grid)
                        or new_col < 0
                        or new_col >= len(grid[0])
                        or grid[new_row][new_col] == -1
                        or grid[new_row][new_col] == 0
                    ):
                        continue
                      
                    new_val = 1 + grid[row][col]
                    if new_val < grid[new_row][new_col]:
                        grid[new_row][new_col] = new_val
                        q.append((new_row, new_col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i, j)

        # return grid