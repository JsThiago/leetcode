import string

#Tempo: O(n), Espaço: O(1)
class Solution:
    def solve(self, s: string):
        start = 0
        end = len(s) - 1
        while start < end:
            if(s[start].islower() and s[end].islower()):
                if(s[start] != s[end]):
                    return False
                start = start + 1
                end = end - 1
            if(not s[start].islower()):
                start = start + 1
            if(not s[end].islower()):
                end = end - 1
        return True

solution = Solution()
print(solution.solve("a92bceXa"))
            