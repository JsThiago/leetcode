class Solution:
    def helper(self,value,cache):

        print(value)
        if(value in cache):
            return cache[value]
        if(value == 1 or value == 0):
            return 0
        for i in range(1,value):
                cache[value] = self.helper(value-i,cache) + self.helper(i,cache)

    def combinationSum4(self, nums: list[int], target: int) -> int:
        cache = {} 
        for num in nums:
            cache[num] = 1
        self.helper(10,cache)
        return aux[-1]


solution = Solution()
solution.combinationSum4([1,2],10)
