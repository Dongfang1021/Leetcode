class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i,j))
        while q:
            x, y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0, -1)]:
                newX, newY = x + dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(mat) - 1 and newY >= 0 and newY <= len(mat[0]) - 1 and (newX, newY) not in visited:
                    mat[newX][newY] = mat[x][y]+1
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return mat