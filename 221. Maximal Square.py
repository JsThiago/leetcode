class Solution:
    def helper(self,i,j,matrix,cache):

        if(i >= len(matrix) or j >= len(matrix[0])):
            return 0
        if((i,j) in cache):
            return cache[(i,j)] 
        baixo = self.helper(i+1,j,matrix,cache)
        direita = self.helper(i,j+1,matrix,cache)
        diagonal = self.helper(i+1,j+1,matrix,cache)
        if(matrix[i][j] == "0"):
            return 0
        cache[(i,j)] = 1+min(baixo,direita,diagonal)

        return cache[(i,j)]


    def maximalSquare(self, matrix: list[list[str]]) -> int:
        cache = {}
        self.helper(0,0,matrix,cache)
        #result = max(cache.values())
        print(len(cache))
        return result * result
solution = Solution()
#print(solution.maximalSquare([["0","0","1","0"],["1","1","1","1"],["1","1","1","1"],["1","1","1","0"],["1","1","0","0"],["1","1","1","1"],["1","1","1","0"]]))
print(solution.maximalSquare([["0"]]))
