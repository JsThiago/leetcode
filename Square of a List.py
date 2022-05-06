#Tempo: O(n), Espaço:O(n)
class Solution:
    def solve(self, nums):
        start = 0
        final = len(nums) - 1
        result = []
        while(start<=final):
            if(pow(nums[start],exp=2) > pow(nums[final],exp=2)):
                result.append(pow(nums[start],exp=2))
                start = start + 1
                continue
            else:
                result.append(pow(nums[final],exp=2))
                final = final - 1
        return list(reversed(result))



solution = Solution()
solution.solve([-2,2])