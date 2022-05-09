class Solution:
    def solve(self, s):
        lastNum = ""
        sum = 0
        for letter in s:
            if(letter.isdigit()):
                lastNum = lastNum + letter
                continue
            if(not letter.isdigit() and len(lastNum) > 0):
                sum = sum + int(lastNum)
                lastNum = ""
                continue
        if(lastNum != ""):
            sum = sum + int(lastNum)
        return sum


solution = Solution()
solution.solve("123a5")