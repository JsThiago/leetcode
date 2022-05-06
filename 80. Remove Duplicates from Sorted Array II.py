class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicate = 0
        i = 0
        while i < len(nums):
            if(i+1 < len(nums)):
                if(nums[i] == nums[i+1] and duplicate >= 1):            
                    nums.pop(i+1)
                    continue
                elif(nums[i]!=nums[i+1]):
                    duplicate = 0
                    i = i + 1
                    continue
                else:
                    i = i + 1
                    duplicate = duplicate + 1
            else:
                break
        return nums
solution = Solution()
solution.removeDuplicates([1,1,1,2,2,3])