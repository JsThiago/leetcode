#Tempo: O(n), Espaço:O(1)
class Solution:
    def solve(self, s):
        direita = 0
        for i in range(len(s)):
            if(s[i] == ")" and direita == 0):
                return False
            if(s[i] == ")"):
                direita= direita - 1
                continue
            if(s[i] == "("):
                direita = direita + 1
                continue
        if(direita>0):
            return False
        return True

solution = Solution()
print(solution.solve("((()))"))