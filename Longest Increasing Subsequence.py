class Solution:
    def solve(self, nums):
        maxN = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            j = 0
            while j < i:
                if(nums[j] < nums[i] and dp[j]+1>dp[i]):
                    dp[i] = dp[j] + 1
                j = j+1
            maxN = max(maxN,dp[i])
        return maxN

solution = Solution()
solution.solve(nums = [1,2,0])