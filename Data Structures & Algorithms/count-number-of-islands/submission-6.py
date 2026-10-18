import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            # check bounds first
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == "0"
            ) : # this condition states that the current index you are checking is beyond the bounds of the grid
                return

            grid[row][col] = "0"

            dfs(row+1, col) # check below
            dfs(row-1, col) # check above
            dfs(row, col+1) # check right
            dfs(row, col-1) # check left


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1


        return islands