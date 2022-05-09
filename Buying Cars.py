class Solution:
    def solve(self, prices, k):
        prices = sorted(prices)
        sum = 0
        count = 0
        for i in range(0,len(prices),1):
            if(prices[i] + sum <= k):
                count = count + 1
                sum = sum + prices[i]
        return count

solution = Solution()
solution.solve([90, 30, 20, 40, 90],95)