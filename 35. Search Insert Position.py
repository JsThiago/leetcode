# Tempo : O(log n) Espaço: O(1)

import math


class Solution:
    nums = []
    target = 0
    def BS(self,inicio,final):
        if(inicio > final or inicio>len(self.nums)-1):
            return -1
        n = math.ceil(((final-inicio)/ 2) + inicio)
        if(self.nums[n] == self.target):
            return n
        elif(self.nums[n] > self.target and self.nums[n-1] < self.target):
            return n
        elif(self.nums[n] < self.target and self.nums[n+1] > self.target):
            return n+1
        if(self.nums[n]<self.target):
            return self.BS(n+1,final)
        else:           
            return self.BS(inicio,n-1)
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        if(len(nums) == 1):
            if(nums[0] < target):
                return 1
            return 0
        if(target > nums[len(nums)-1]):
            return len(nums)
        if(target < nums[0]):
            return 0
        self.nums = nums
        self.target = target
        n = math.ceil((len(nums)-1)/2)
        if(nums[n] == target):
            return n
        elif(nums[n] > target and nums[n-1] < target):
            return n
        elif(nums[n] < target and nums[n+1] > target):
            return n+1
        elif(nums[n] > target):
            return self.BS(0,n)
        else:
            print("n",n,len(nums)-1)
            return self.BS(n,len(nums)-1)

solution = Solution()
print(solution.searchInsert([1,3],4))