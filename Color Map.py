#binarySearch.com
#Tempo: O(n^2), Espaço: O(n^2)

class Solution:

    def createMatrix(self,c,l):
        m = [0] * l
        for i in range(l):
            m[i] = [-1] * c
        return m

        
    def bfs(self,matrix,m,hash,x,y,c,l):
        stack = [(x,y)]
        if(x < 0 or x >= l or y < 0 or y >= c):
            return
       
        numero = matrix[x][y]
        if(m[x][y] != -1):
            return
        m[x][y] = 1
        while len(stack) > 0:
            (xt,yt) = stack.pop(-1)
            for i in [(1,0),(0,1),(0,-1),(-1,0)]:
                if((i[0] + xt) >= 0 and (i[0] + xt) < l and (i[1]+ yt) >= 0 and (i[1] + yt) < c and m[i[0] + xt][i[1] + yt] == -1):
                    if(matrix[xt+i[0]][yt+i[1]] == numero):
                        m[i[0] + xt][i[1]+ yt] = 1
                        stack.append((xt+i[0],yt+i[1]))
        if(numero in hash):
            hash[numero] = hash[numero] + 1
        else:
            hash[numero] = 1



    def solve(self, matrix):
        if(len(matrix) == 0):
            return 0
        c = len(matrix[0])
        l = len(matrix)
        hash = {}
        maxN = -1
        m = self.createMatrix(len(matrix[0]),len(matrix))
        for i in range(c):
            for j in range(l):        
                self.bfs(matrix,m,hash,j,i,c,l)
        sum = 0
        maxK= 0
        for i in hash:
            if(hash[i] > maxN):
                maxN = hash[i]
                maxK = i
       
        for i in hash:
            if(i !=maxK):
                sum = sum + hash[i]
                
        print(sum)
        return sum
solution = Solution()
solution.solve(matrix = [
    [1, 2]
])