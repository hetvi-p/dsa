class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        nr, nc = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r: int, c: int, grid: List[List[str]]):

            visited.add((r,c))

            for dr, dc in directions:
                if ((r + dr) in range(nr) and (c + dc) in range(nc) and 
                grid[r + dr][c + dc] == "1" and (r+dr, c+dc) not in visited):
                    visited.add((r + dr, c + dc))
                    dfs(r + dr, c + dc, grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c, grid)
                    islands += 1

        return islands

                

                




                
