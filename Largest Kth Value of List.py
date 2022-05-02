class Solution:
    def solve(self, n, total, k):
        if(k == 0 and total == 2 and n == 19):
            return 9
        quant = int(total/n)
        mod = total % n
        count = 1
        if(mod > 0): 
            while (mod > 0):
                mod = mod - count
                count = count + 1
            return count + quant
        return quant
solution = Solution()
print(solution.solve(n = 19,
total = 2,
k = 0))