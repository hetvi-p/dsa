class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cboard = [row[:] for row in board]
        nr = len(board)
        nc = len(board[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

        for r in range(nr):
            for c in range(nc):
                if cboard[r][c] == 0:
                    count = 0
                    for dr, dc in directions:
                        if ((r + dr) in range(nr) and (c + dc) in range(nc) and 
                        cboard[r + dr][c + dc] == 1):
                            count += 1
                    if count == 3:
                        board[r][c] = 1
                
                if cboard[r][c] == 1:
                    count = 0
                    for dr, dc in directions:
                        if ((r + dr) in range(nr) and (c + dc) in range(nc) and
                        cboard[r + dr][c + dc] == 1):
                            count += 1
                    if count < 2 or count > 3:
                        board[r][c] = 0

        return


        