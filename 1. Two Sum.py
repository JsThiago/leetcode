
# Tempo: O(n) Espaço: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        for index,num in enumerate(nums):
            print("hash",hash) 
            search = target - num
            print("search",search)
            if(search in hash):
                return (hash[search],index)
            hash[num] = index

solution = Solution()
print(solution.twoSum([2,7,11,15],9))