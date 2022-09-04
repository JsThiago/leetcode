class Solution:
    def helper(self,array):
        print(array)
        if(len(array) == 1):
            return array[0]
        if(len(array) == 0):
            return 0
        part1 = int(len(array)/2)
        part2 = int(len(array)/2) + 1
        return max(sum(array),self.helper(array[0:part1]),self.helper(array[part1:len(array)]))

    def maxSubArray(self, nums: list[int]) -> int:
           result = self.helper(nums) 
           print(result)

solution = Solution()
solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
