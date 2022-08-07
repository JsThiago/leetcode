class Solution:
    def helper(self,_sum,sums,value,cache,array,index):
        for i in range(index,len(array)):
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
        self.helper(0,[],target,result,candidates,0) 
        return result

solution = Solution()
solution.combinationSum(candidates = [2,3,6,7], target = 7)
        
