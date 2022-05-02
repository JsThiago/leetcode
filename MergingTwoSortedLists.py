#Tempo: O(n), Espaço: O(n)
class Solution:
    def solve(self, a, b):
        j = 0
        i = 0
        result = []
        while j < len(b) or i < len(a):
            print(j,i)
            if(i < len(a) and j < len(b)):
                if(a[i]<b[j]):
                  
                    result.append(a[i])
                    i = i + 1
                    continue
                if(b[j]<=a[i]):
                    result.append(b[j])
                    j = j + 1
                    continue
            if(i < len(a)):
                result.append(a[i])
                i = i + 1
                continue
            if(j < len(b)):
                result.append(b[j])
                j = j + 1
                continue
        print(result)

solution = Solution()
solution.solve(a = [5, 10, 15],b = [3, 8, 9])
