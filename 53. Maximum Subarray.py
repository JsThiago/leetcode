

# Tempo:O(n) Espaço: O(1)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        i = 1
        sum = nums[0]
        oldSoma = sum
        while(i<len(nums)):
            if(nums[i] > sum and sum < 0):
                print("substitui:",nums[i])
                sum = nums[i]
            elif(nums[i] > 0):
                print("soma",nums[i])
                sum = sum+ nums[i]
            elif(i+1<len(nums) and sum + nums[i] + nums[i+1] >= nums[i+1]):
                if(sum + nums[i] + nums[i+1] < sum and sum > oldSoma):
                    oldSoma = sum
                print("soma",nums[i],nums[i+1])
                sum = sum + nums[i] + nums[i+1]
                i = i + 2
                continue
            else:
                if(oldSoma < sum):
                    oldSoma = sum
                sum = nums[i]
            i = i+1
        return max(oldSoma,sum)

solution = Solution()
print("result",solution.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))