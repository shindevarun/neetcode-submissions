class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0

    #     rows, cols = len(grid), len(grid[0])
    #     islands = 0

    #     def dfs(row, col):
    #         # check bounds first
    #         if (
    #             row < 0
    #             or row >= len(grid)
    #             or col < 0
    #             or col >= len(grid[0])
    #             or grid[row][col] == "0"
    #         ) : # this condition states that the current index you are checking is beyond the bounds of the grid
    #             return

    #         grid[row][col] = "0"

    #         dfs(row+1, col) # check below
    #         dfs(row-1, col) # check above
    #         dfs(row, col+1) # check right
    #         dfs(row, col-1) # check left


    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == "1":
    #                 dfs(row, col)
    #                 islands += 1


    #     return islands



    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def bfs(row, col):
            q = collections.deque()
            grid[row][col] = "0"
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
                        or grid[new_row][new_col] == "0"
                    ) :
                        continue

                    grid[new_row][new_col] = "0"
                    q.append((new_row, new_col))
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands
