#Tempo: O(n), Espaço:O(n)
# class Solution:
#     def solve(self, nums):
#         start = 0
#         final = len(nums) - 1
#         result = []
#         while(start<=final):
#             if(pow(nums[start],exp=2) > pow(nums[final],exp=2)):
#                 result.append(pow(nums[start],exp=2))
#                 start = start + 1
#                 continue
#             else:
#                 result.append(pow(nums[final],exp=2))
#                 final = final - 1
#         return list(reversed(result))

class Solution:
    def solve(self, nums):
        start = 0
        final = len(nums) - 1
        while(start<=final):
            if(start == final):
                nums[final] = pow(nums[final],2)
            if(pow(nums[final],2)<=pow(nums[start],2)):
                change = nums[final]
                nums[final] = pow(nums[start],2)
                nums[start] = change
            else:
                nums[final] = pow(nums[final],2)              
            final = final - 1
        print(nums)
        return nums


solution = Solution()
solution.solve([-2,2])