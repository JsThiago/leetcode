class Solution:
    def helper(self,k,n,_sum,array,nums,result,index):
        if(len(nums)>k or _sum > n):
            return 
        for i in range(index,len(array)):
            if(len(nums) > 0 and array[i] == nums[len(nums)-1]):
                continue
            newSum = _sum + array[i]
            nums.append(array[i])
            if(newSum > n or len(nums)>k):
                break
            if(newSum == n and len(nums) == k):
                result.append(nums[:])
            self.helper(k,n,newSum,array,list(nums[:]),result,i)
            nums.pop()

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        numbers = []
        result = []
        for i in range(1,10):
            if(i<n):
                numbers.append(i)
        self.helper(k,n,0,numbers,[],result,0)
        print(result)
        return result

solution = Solution()
solution.combinationSum3(3,9)
