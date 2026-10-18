# 2 solutions: DFS & BFS

# Key idea is this: we iterate through every node in the grid. If that node is a "1", we have stumbled across an island.
# Then we launch into DFS/BFS algorithm.
# First mark that current node to 0 to indicate "visited". Don't need to have a explicit visited list, making that node 0 serves the same purpose.
# Then, check every neighbor (4) of that current node. For neighbors that are not out of bounds of the grid or 0, this are of interest
# since this is another legally adjacent 1 (extension of the island). You will want to then for each of these extensions, repeat the same process.
# First mark it 0, then check it's 4 neighbors. This will keep happening until all of the legally adjacent 1's have been converted to 0s.
# So we just got rid of that entire island from the grid. Then when we break out of the BFS/DFS and return to our solution, we can increment
# numIslands since we removed an entire island from the grid. When you keep doing this on every element in the grid, you will run overall
# DFS/BFS only when you find a completely distinct island since you got rid of all already discovered islands!

class Solution:
    # DFS solution
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


    # BFS solution: Essentially the same thing but we solve it iteratively using a queue to keep track of what nodes to visit next
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

                for direction in directions: # we check every direction of current node
                    new_row, new_col = row + direction[0], col + direction[1]

                    if (
                        new_row < 0
                        or new_row >= len(grid)
                        or new_col < 0
                        or new_col >= len(grid[0])
                        or grid[new_row][new_col] == "0"
                    ) :
                        continue # if ajacent is out of bound or water, continue to next iteration. don't add to queue

                    grid[new_row][new_col] = "0"
                    q.append((new_row, new_col))
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands
