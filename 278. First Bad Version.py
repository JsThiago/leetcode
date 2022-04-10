# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:



# Tempo: O(log n) Espaço: O(1)
import math
def isBadVersion(n):
    if(n >= 2147483546):      
        return True
    return False
class Solution:
    def aux(self,inicio,fim):
        n = math.ceil((inicio+fim)/2)       
        if(isBadVersion(n) is True and isBadVersion(n-1) is False):                     
            return n
        if(isBadVersion(n) is False and isBadVersion(n+1) is True):                
            return n+1
        if(isBadVersion(n) is False):
            return self.aux(n,fim)
        return self.aux(inicio,n)
    
    
    def firstBadVersion(self, n: int) -> int:
        len = n
        n = math.ceil(n/2)
        if(isBadVersion(n) is True and isBadVersion(n-1) is False):                     
            return n
        if(isBadVersion(n) is False and isBadVersion(n+1) is True):                
            return n+1
        if(isBadVersion(n) is True):            
            return self.firstBadVersion(n)
        else:
            return self.aux(n,len)
        
solution = Solution()
print(solution.firstBadVersion(2147483647))