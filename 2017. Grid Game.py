class Solution:
    

    def gridGame(self, grid: list[list[int]]) -> int:
       sumCima = grid[0][:]
       sumBaixo = grid[1][:]
       for i in range(1,len(grid[0])):
            sumBaixo[i] = sumBaixo[i-1] + sumBaixo[i]
            sumCima[i] = sumCima[i-1] + sumCima[i]
       print(sumCima)
       minRobot2 = min(sumCima[len(sumCima)-1]-sumCima[0],sumBaixo[0])
       i = 0
       for i in range(1,len(grid[0])):
           minRobot2 = min(max(sumCima[len(sumCima) - 1] - sumCima[i],sumBaixo[i-1]),minRobot2)
       return minRobot2 

solution = Solution()
print(solution.gridGame([[3,3,1],[8,5,2]]))

