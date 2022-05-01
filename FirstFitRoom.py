#Binarysearch.com
#Tempo: O(n), Espaço: (1)
class Solution:
    def solve(self, rooms, target):
        for i in rooms:
            if(i >= target):
                return i
        return -1