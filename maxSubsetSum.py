#Tempo: O(n), Espaço: O(1)
#hackerRank
def maxSubsetSum(values:list):
    maxN = max(0,values[len(values)-1])
    lastSum = max(0,values[len(values)-2])
    for i in range(len(values)-3,-1,-1):
        print(lastSum,maxN,i)
        aux = lastSum
        lastSum = max(values[i]+maxN,values[i],0)
        maxN = max(aux,maxN)
    return maxN
        
maxSubsetSum([2, 1 ,5, 8, 4])