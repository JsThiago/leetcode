from msvcrt import kbhit


class Solution:
    def solve(self, values, k):
        if(len(values) == 1):
            return values[0]
        dp = [0] * len(values)
        for i in range(1,len(values)):           
            j = i-1
            while j >= 0:
                if(dp[j]+values[i] <= k and values[i]+values[j]<=k):
                    dp[i] = max(dp[j]+values[i],values[i]+values[j],dp[i])                                     
                elif(dp[j]+values[i] <= k):
                    dp[i] = max(dp[j]+values[i],dp[i])                                
                elif(values[j]+values[i] <= k):
                    dp[i] = max(values[j]+values[i],dp[i])                   
                j = j - 1
        print(dp)
solution = Solution()
solution.solve(
values = [ -1, 2, 2],
k = 4)
