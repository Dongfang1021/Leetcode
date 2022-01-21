class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
    
        n = len(isConnected)
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= n or isConnected[row][col] != 1:
                return
            isConnected[row][col] = 2
            isConnected[col][row] = 2
            
            for i in range(n):
                if isConnected[row][i] == 1:
                    dfs(i, row)
            
        count = 0 
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    count += 1
                    dfs(row, col)
        return count