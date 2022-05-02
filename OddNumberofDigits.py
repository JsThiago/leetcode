
# Tempo: O(n*k) onde k é o valor de digitos do número que possui maior quantidade de dígitos
# Espaço: O(1)
class Solution:
    def solve(self, nums):
        result = 0
        for num in nums:
            aux = num
            count = 0
            while(aux > 0):             
                aux = int(aux/10)
                count = count + 1                
            if(count % 2 != 0):         
                result = result + 1
        print(result)

solution= Solution()

solution.solve(nums = [1, 800, 2, 10, 3])