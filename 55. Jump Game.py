class Solution:
    def canJump(self, nums: list[int]) -> bool:
        lastIndex = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            print(lastIndex,i,nums[i])
            if(((lastIndex - i)-nums[i])<=0):
                lastIndex = i
                continue
        print(lastIndex)
        return lastIndex == 0


solution = Solution()
solution.canJump([3,2,1,0,4])
