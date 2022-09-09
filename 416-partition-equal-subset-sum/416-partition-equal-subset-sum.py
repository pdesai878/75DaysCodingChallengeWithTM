class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # s1=s2
        # s1+s2=sum
        # s1-s2=0
        # 2s1=sum
        # s1=sum//2
        # if s1 exists, then partition possible
     
        sum_=sum(nums)
        if sum_&1:
            return False
        target=sum_//2
        n=len(nums)
        if n==1:
            return nums[0]==target
        dp=[[False for j in range(target+1)]for i in range(2)] 
        for row in range(2):
            dp[row][0]=True
        
        for i in range(1,n):
            for j in range(1,target+1):
                if nums[i]<=j:
                    dp[i&1][j]=dp[(i-1)&1][j-nums[i]] or dp[(i-1)&1][j]
                else:
                    dp[i&1][j]=dp[(i-1)&1][j]
        return dp[i&1][-1]
                
                
       
       
        
            
            
        
        
        