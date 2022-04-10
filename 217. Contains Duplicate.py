#Tempo: O(n) Espaço: O(n) 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for num in nums:
            if(num in hash):
                return True
            hash[num] = 1
        return False
solution = Solution()
print(solution.containsDuplicate([1,2,3,4]))