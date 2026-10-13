class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            s = set()

            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)       


        # cols
        for i in range(9):
            s = set()

            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)  

        
        # squares
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]


        for i,j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col] != ".":
                        s.add(board[row][col])

        return True
