
#BinarySearch.com
#Tempo: O(n), Espaço: O(n)
import math


class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node:LLNode):
        stack = []
        aux = node
        if(node == None):
            return None
        while(aux != None):
            stack.append(aux.val)
            aux = aux.next
        middle = stack[math.floor(len(stack)/2)]
        return middle

        


node1 = LLNode(0)
node2 = LLNode(1)
node3 = LLNode(2)
node1.next = node2
node2.next = node3

solution = Solution()
solution.solve(node1)