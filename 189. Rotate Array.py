# Tempo: O(k) Espaço: O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(0,k):
            nums.insert(0,nums.pop())
        """
        Do not return anything, modify nums in-place instead.
        """


solution = Solution()
nums = [-1,-100,3,99]
solution.rotate(nums,2)
print(nums)