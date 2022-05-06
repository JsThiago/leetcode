#Somente funciona para valores positivos
class Solution:

        
    def solve(self, n, total, k):
        array = [0] * n
        while total>0:
            if(k+1<len(array)):
                if(abs(array[k] - array[k+1]) + 1 > 1):
                    aux = k + 1
                    while aux + 1 < len(array) or total > 0:
                        if(aux + 1 >= len(array)):
                            break
                        if(abs(array[aux] - array[aux + 1])+1 > 1):
                            array[aux] = array[aux] + 1
                            total = total - 1
                            aux = aux + 1
                            continue
                        break
                    if(aux == len(array) - 1):
                        array[aux] = array[aux] + 1
                        total = total - 1
            if(k-1>=0):
                if(abs(array[k] - array[k-1]) + 1 > 1):
                    aux = k - 1
                    while aux - 1 >= 0 or total > 0:
                        if(aux - 1 < 0):
                                break
                        if(abs(array[aux] - array[aux + 1])+1 > 1):
                            array[aux] = array[aux] + 1
                            total = total - 1
                            aux = aux - 1                 
                            continue
                        break
                    if(aux == 0):
                        array[aux] = array[aux] + 1
                        total = total - 1
            array[k] = array[k] + 1
            total = total - 1
        return array[k]