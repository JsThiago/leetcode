#Binarysearch.com
#Tempo:O(n/2), Espaço: O(1)
class Solution:
    def solve(self, s):
        i = 0
        j = len(s) - 1
        while(i<j):
            if(s[i] != s[j]):
                return False
            i = i + 1
            j = j - 1
        return True