class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:
            return matrix[0][0]
        mn=sys.maxsize
        dp=[[0 for j in range(n)]for i in range(2)]
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i==n-1:
                    dp[i&1][j]=matrix[i][j]
                    continue
                if j==0:
                    dp[i&1][j]=matrix[i][j]+min(dp[(i+1)&1][j],dp[(i+1)&1][j+1])
                elif j==n-1:
                    dp[i&1][j]=matrix[i][j]+min(dp[(i+1)&1][j],dp[(i+1)&1][j-1])
                else:
                    dp[i&1][j]=matrix[i][j]+min(dp[(i+1)&1][j],dp[(i+1)&1][j-1],dp[(i+1)&1][j+1])
                    
        
        # print(dp)
        return min(dp[i&1])
        
        