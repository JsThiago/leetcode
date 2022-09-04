class Solution:
    def helper(self,start,nums,pos,dp):
        if(start ==0 and pos == len(nums) - 1):
            return 0
        if(pos in dp):
            return dp[pos]
        jump1 = 0
        jump2 = 0
        if(abs(((pos+2)%len(nums))-start) > 1 and abs(((pos+2)%len(nums))-pos) > 1):
            jump1 = self.helper(start,nums,(pos+2)%len(nums),dp)
        if(abs(((pos+3)%len(nums))-start) > 1 and abs(((pos+3)%len(nums))-pos) > 1):
            jump2 = self.helper(start,nums,(pos+3)%len(nums),dp)
        dp[pos] = nums[pos] + max(jump1,jump2)
        return dp[pos]
        

    def rob(self, nums: list[int]) -> int:
       if(len(nums)<3):
           return max(nums)
       result = max(self.helper(0,nums,0,{}),self.helper(1,nums,1,{}),self.helper(2,nums,2,{}))
       return result


solution = Solution()
solution.rob([6,6,4,8,4,3,3,10])
