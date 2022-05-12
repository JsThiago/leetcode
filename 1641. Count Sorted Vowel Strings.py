class Solution:
    def countVowelStrings(self, n: int) -> int:
        globalSum = 5
        if(n == 1):
            return 5
        dp = [4,3,2,1]
        i = 0
        while(i<n-1):
            sumN = sum(dp)
            globalSum = globalSum + sumN
            dp[0] = sumN
            dp[1] = dp[1] + dp[2] + dp[3]
            dp[2] = dp[2] + dp[3]
            i = i + 1
        print(globalSum)
        return globalSum

solution = Solution()
solution.countVowelStrings(3)
