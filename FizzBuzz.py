class Solution:
    def solve(self, n):
        result = []
        for i in range(1,n+1):
            if(i % 3 == 0 and i % 5 == 0):
                result.append("FizzBuzz")
                continue
            if(i % 3 == 0):
                result.append("Fizz")
                continue
            if(i % 5 == 0):
                result.append("Buzz")
                continue
            else:
                result.append(str(i))
        return result

solution = Solution()
solution.solve(15)

