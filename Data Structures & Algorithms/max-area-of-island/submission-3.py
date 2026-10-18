# Same approach as number of islands problem but now everytime you mark an island node as visited, you increment area of that island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0


        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxArea = 0

        def bfs(row, col):
            q = collections.deque()
            grid[row][col] = 0
            q.append((row, col))
            currArea = 1

            while q:
                row, col = q.popleft()

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]

                    if (
                        new_row < 0
                        or new_row >= len(grid)
                        or new_col < 0
                        or new_col >= len(grid[0])
                        or grid[new_row][new_col] == 0
                    ) :
                        continue

                    q.append((new_row, new_col))
                    currArea += 1
                    grid[new_row][new_col] = 0

            return currArea


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currArea = bfs(i, j)
                    if currArea > maxArea:
                        maxArea = currArea

        return maxArea