class Solution:
    def dfs(self,n,m,i,j,cache):
        if(i >= m or j >= n):
            return 0
        if((i,j) in cache):
            return cache[(i,j)]
        if(i == m-1 and j == n-1):
            return 1
        
        
        bottom = self.dfs(n,m,i+1,j,cache)
        right = self.dfs(n,m,i,j+1,cache)
        cache[(i,j)] = bottom + right
        return cache[(i,j)]


    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.dfs(n,m,0,0,cache)


solution = Solution()
print(solution.uniquePaths(3,7))
