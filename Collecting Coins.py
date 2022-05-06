class Solution:
    def createMatrix(self,l,c):
        m = [0] * l
        for i in range(l):
            m[i] = [0] * c
        return m

    def solve(self, matrix):
        c = len(matrix[0])
        l = len(matrix)
        m = self.createMatrix(l,c)
        m[0][0]=matrix[0][0]+1
        for i in range(l):
            for j in range(c):
                if(i+1 < l):
                    if(m[i][j] != 0):
                        if(m[i][j]+matrix[i+1][j] >= m[i+1][j]):
                            m[i+1][j] = m[i][j]+matrix[i+1][j]
                    else:
                        m[i+1][j] = matrix[i][j] + matrix[i+1][j]
                if(j+1 < c):
                   if(m[i][j] != 0):
                        if(m[i][j]+matrix[i][j+1] >= m[i][j+1]):
                            m[i][j+1] = m[i][j]+matrix[i][j+1]
                   else:
                            
                        m[i][j+1] = matrix[i][j] + matrix[i][j+1]
        return m[-1][-1]-1