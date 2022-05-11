# Tempo: O(n), Espaço: O(1)
class Solution:
    def solve(self, nums):
        lastNum = -1
        count = 0
        for num in nums:
            if(num != lastNum):
                lastNum = num
                count = count + 1
        return count



solution = Solution()
solution.solve([2, 2, 2, 3, 4, 6, 6])