class Solution:
    pos={
        "up":{
            "y":0,
            "x":-1
        },
        "down":{
            "y":0,
            "x":1
        },
        "right":{
            "y":1,
            "x":0
        },
        "left":{
            "y":-1,
            "x":0
        }
    }
    def isValid(self,x,y,l,c):
        
        if(x < 0 or y < 0 or x >= l or y>=c):
            return False
        return True
    
    def dfs(self,x,y,hash,m,l,c):
        
       
        if(not self.isValid(x,y,l,c)):
          
            return 0
        if(hash[x][y] != -1):
             
            return hash[x][y]
        moves = 0
      
        if(self.isValid(x+self.pos["down"]["x"],y+self.pos["down"]["y"],l,c)):
            if(m[x+self.pos["down"]["x"]][y+self.pos["down"]["y"]] > m[x][y]):
                moves = 1 + self.dfs(x+self.pos["down"]["x"],y+self.pos["down"]["y"],hash,m,l,c)
        
        if(self.isValid(x+self.pos["up"]["x"],y+self.pos["up"]["y"],l,c)):
            print(x,y)
            if(m[x+self.pos["up"]["x"]][y+self.pos["up"]["y"]] > m[x][y]):
                retorno = 1 + self.dfs(x+self.pos["up"]["x"],y+self.pos["up"]["y"],hash,m,l,c)
                if(moves < retorno):
                    moves = retorno
        
        if(self.isValid(x+self.pos["right"]["x"],y+self.pos["right"]["y"],l,c)):
          
            if(m[x+self.pos["right"]["x"]][y+self.pos["right"]["y"]] > m[x][y]):
                retorno = 1 + self.dfs(x+self.pos["right"]["x"],y+self.pos["right"]["y"],hash,m,l,c)
                if(moves < retorno):
                    moves = retorno 
        
        if(self.isValid(x+self.pos["left"]["x"],y+self.pos["left"]["y"],l,c)):
            if(m[x+self.pos["left"]["x"]][y+self.pos["left"]["y"]] > m[x][y]):
                retorno = 1 + self.dfs(x+self.pos["left"]["x"],y+self.pos["left"]["y"],hash,m,l,c)
                if(moves < retorno):
                    moves = retorno         
        hash[x][y] = moves
        return moves
    
    
    def generateMatrix(self,l,c):
        m = [0] * l
        for i in range(l):
            m[i] = [-1] * c
        return m
    def longestIncreasingPath(self, matrix) -> int:
        l = len(matrix)
        c = len(matrix[0])
        m = self.generateMatrix(len(matrix),len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(i,j,m,matrix,l,c)
        maxValue = 0
        for i in range(len(m)):
            maxValue = max(maxValue,max(m[i]))
        return maxValue + 1


solution = Solution()
solution.longestIncreasingPath(
    [[2147483647,1]])