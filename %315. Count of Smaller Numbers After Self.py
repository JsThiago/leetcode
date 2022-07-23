class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
       size = len(nums)
       last = []
       result = []
       for i in range(size-1,-1,-1):
           if(i == size-1):
              last.append({"quant":0,"number":nums[i]})
              result.append(0)
              continue
           sizeLast = len(last)
           found = False
           smallThanAll = 0
           for j in range(sizeLast-1,-1,-1):
               print(i)
               if(last[j]["number"]<nums[i] and last[j]["number"]>0):
                   last.append({"quant":last[j]["quant"]+1+smallThanAll,"number":nums[i]})
                   result.append(last[j]["quant"]+1+smallThanAll)
                   found = True
                   break
               if(last[j]["number"] == 0):
                   smallThanAll = smallThanAll + 1
           if(found is False):
               result.append(0)
               last.append({"quant":0,"number":nums[i]})

       result.reverse()
       print(result)


solution = Solution()
print(solution.countSmaller([2,0,1]))
