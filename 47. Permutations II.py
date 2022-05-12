class Solution:


    def bt(self,nums,matrix,arr,pos):
        for i in range(len(nums)):
            if(len(arr) == len(nums)):
                matrix.append(arr[:])
                return
            if(i in pos):
                continue
            pos.append(i)
            arr.append(nums[i])
            self.bt(nums,matrix,arr,pos)
            pos.pop()
            arr.pop()
              
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        matrix = []
        self.bt(nums,matrix,[],[])
        return matrix

solution = Solution()
solution.permuteUnique([1,2,3])