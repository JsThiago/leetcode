import math
import string
from time import sleep

#Não feito
class Solution:
        
    def solve(self, a:string, b:string):
        hash = {}
        for i in range(len(a)):
            if(not a[i] in hash):
                hash[a[i]] = []
            j = i + 1
            arr = [{},0]
            while j < len(a):
                arr[0][a[j]] = 1
                j = j + 1
            arr[1] = i
            hash[a[i]].append(arr)
        globalCount = 0
        print(hash)
        for i in range(len(b)):
            
            if(b[i] not in hash):
                continue
            
            j = i + 1
            actual = b[i]
            posActual = i
            count = 1
            
            while j < len(b):
                if(b[j] in hash[actual]):
                    for value in hash[actual]:
                        if(value[1] > hash[actual][1]):
                            count = count + 1
                            actual = b[i]
                            posActual = hash[actual][1]
                j=j+1

            globalCount = max(count,globalCount)
        print(globalCount)
        return globalCount

solution = Solution()
solution.solve(

a = "ourkuxbpok",
b = "ufquoxhppc")