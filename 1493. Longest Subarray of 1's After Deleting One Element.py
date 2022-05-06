#Tempo: O(N), Espaço: O(1)
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        bz = 0
        az = 0
        quantz = 0
        lastGreaterSum = 0
        for num in nums:
            if(quantz == 1 and num == 0):
                lastGreaterSum = max(az + dz,lastGreaterSum)
                bz = az
                az = 0
                continue
            if(quantz == 1 and num == 1):
                az = az + 1
                continue
            if(quantz == 0 and num == 1):
                bz = bz + 1
                continue
            if(num == 0 and quantz == 0):
                quantz = quantz + 1
        if(quantz == 0 and bz+az > 0):
            return az+bz-1
        return max(lastGreaterSum,bz+az)

solution = Solution()
solution.longestSubarray([1,0,0,0,0])