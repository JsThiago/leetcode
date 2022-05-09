class Solution:
    def solve(self, nums):
        globalSum = -9999999
        lastSum = 0 
        for num in nums:
            lastSum = lastSum + num
            if(globalSum<lastSum):
                globalSum = lastSum
            if(lastSum<0):
                lastSum = 0
        return globalSum

solution = Solution()
solution.solve([-1,-2,-3])