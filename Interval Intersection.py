#Tempo:O(n), Espaço:O(1)
class Solution:
    def solve(self, intervals):
        initial = intervals[0][0]
        final = intervals[0][1]
        for interval in intervals:
            if(interval[0] > initial):
                initial = interval[0]
            if(interval[1] < final):
                final = interval[1]
        return [initial,final]

solution = Solution()
solution.solve([
    [1, 100],
    [10, 50],
    [15, 65]
])