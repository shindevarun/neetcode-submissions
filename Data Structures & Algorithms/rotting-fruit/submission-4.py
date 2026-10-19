class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0,1], [0,-1]]
        rotten = []
        self.minutes = 0

        if (all(val == 0 for row in grid for val in row)):
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        def bfs(rotten):
            q = collections.deque()
            
            for coord in rotten:
                q.append(coord)
            
            while q:
                level = len(q)

                for i in range(level):
                    row, col = q.popleft()
                    
                    for direction in directions:
                        new_row, new_col = row + direction[0], col + direction[1]

                        if (
                            new_row < 0
                            or new_row >= len(grid)
                            or new_col < 0
                            or new_col >= len(grid[0])
                            or grid[new_row][new_col] != 1
                        ):
                            continue

                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))

                self.minutes += 1

        bfs(rotten)

        # if any fresh bananas remain after BFS is done
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return self.minutes - 1