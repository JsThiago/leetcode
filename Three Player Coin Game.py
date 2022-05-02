#Tempo: O(n log n), Espaço: O(1)
class Solution:
    def solve(self, piles):
        piles = sorted(piles)
        print(piles)
        final = len(piles)
        start = -1
        result = 0
        while(True):
            start = start + 1         
            final = final - 2
            if(start>final):
                break
            result = result + piles[final]
        return result
solution = Solution()
solution.solve([2, 4, 1, 3, 5, 6])
