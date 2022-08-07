class Solution:
    def helper(self,_sum,sums,value,cache,array,index):
        for i in range(index,len(array)):
            if(i>0 and array[i] == array[i-1]):
                continue
            if(_sum+array[i]>value):
                break
            sums.append(array[i])
            newSum = _sum + array[i]
            if(newSum == value):
                cache.append(sums)
                break
            self.helper(newSum,sums[0:],value,cache,array,i)
            sums.pop()
        return 

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        self.helper(0,[],target,result,candidates,0) 
        return result
