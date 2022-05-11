class Solution:
    def createArray(self,n):
        a = []
        if(n>=9):
            a = [0] * 9
            for i in range(1,10):
                a[i-1] = i
        else:
            a = [0] * n
            for i in range(1,n+1):
                a[i-1] = i
        return a

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        a = self.createArray(n)
        i = 0
        initialLen = len(a)
        result = []
        hash = {}  
        while i < initialLen:
            lastSize = len(a)
            if(i not in hash):
                hash[i] = [a[i]] 
            for j in range(i+1,lastSize):
                if(a[i] + a[j] <= n):
                    if(j < initialLen):
                        hash[len(a)] = [a[i],a[j]]
                        if(a[i]+a[j] == n and k == 2):
                            result.append([a[i],a[j]])
                        a.append(a[i]+a[j])
                        continue
                    if(not a[i] in hash[j]):           
                        hash[len(a)] = hash[j][:]
                        hash[len(a)].append(a[i])
                        if(a[i]+a[j] == n and (len(hash[j])+1) == k):
                            result.append(sorted(hash[len(a)]))
                        a.append(a[i] + a[j])
            i = i + 1
        resultFilter = []
        for r in result:
            if(not r in resultFilter):
                resultFilter.append(r)
        return resultFilter

        
solution = Solution()
solution.combinationSum3(2,6)