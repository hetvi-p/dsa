class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        nr, nc = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r: int, c: int):

            q = collections.deque()
            q.append((r,c))

            while q:
                r , c = q.popleft()
                for dr, dc in directions:
                    if ((r + dr) in range(nr) and (c + dc) in range(nc) and
                    grid[r + dr][c + dc] == "1" and (r + dr, c + dc) not in visited):
                        visited.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))


        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands

                
