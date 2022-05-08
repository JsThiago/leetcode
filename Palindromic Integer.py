class Solution:
    def solve(self, num):
        stringNum = str(num)
        j = len(stringNum) - 1
        i = 0
        while i < j:
            if(stringNum[i] != stringNum[j]):
                return False
            i = i + 1
            j = j - 1
        return True

solution = Solution()
print(solution.solve(1212))

