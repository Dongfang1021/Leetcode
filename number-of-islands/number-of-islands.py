class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # run bfs
                    islands += 1
                    dq.append([i, j])
                    grid[i][j] = '-1'
                    while dq:
                        x, y = dq.popleft()
                        if x - 1 >= 0:
                            if grid[x - 1][y] == '1':
                                grid[x - 1][y] = '-1'
                                dq.append([x - 1, y])

                        if y - 1 >= 0:
                            if grid[x][y - 1] == '1':
                                grid[x][y - 1] = '-1'
                                dq.append([x, y - 1])

                        if x + 1 < m:
                            if grid[x + 1][y] == '1':
                                grid[x + 1][y] = '-1'
                                dq.append([x + 1, y])

                        if y + 1 < n:
                            if grid[x][y + 1] == '1':
                                grid[x][y + 1] = '-1'
                                dq.append([x, y + 1])
        return islands