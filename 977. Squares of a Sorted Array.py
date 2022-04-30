import math
# Tempo: O(n) Espaço: O(n) 
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        right = len(nums) - 1
        left = 0
        square = [0] * (right + 1)
        print(square)
        while(right>=left):
            print(right,left)
            if(pow(nums[right],2) > pow(nums[left],2)):
                square[right-left] = pow(nums[right],2)
                right = right - 1
                continue
            if(pow(nums[right],2) <= pow(nums[left],2)):
                square[right-left] = pow(nums[left],2)
                left = left + 1
                continue
        return square
# Tempo: O(nlogn) Espaço: O(n) 
class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        square = []
        for num in nums:
            square.append(pow(num,2))
        return sorted(square)
solution = Solution()
print(solution.sortedSquares([-7,-3,2,3,11]))