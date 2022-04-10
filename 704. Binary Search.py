import math

# Tempo: O(n) Espaço: O(n)
class Solution:
    nums = []
    target = 0
    def BS(self,inicio,final):
        if(inicio > final or inicio>len(self.nums)-1):
            return -1
        n = math.ceil(((final-inicio)/ 2) + inicio)
        if(self.nums[n] == self.target):
            return n
        if(self.nums[n]<self.target):
            return self.BS(n+1,final)
        else:           
            return self.BS(inicio,n-1)


    def search(self, nums: list[int], target: int) -> int:
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        self.nums = nums
        self.target = target
        n = math.ceil(len(nums)/2)
        if(nums[n] == target):
            return n
        if(nums[n]<target):
            return self.BS(n+1,len(nums))
        else:
            return self.BS(0,n-1)

solution = Solution()
print(solution.search([-1,0,3,5,9,12],9))