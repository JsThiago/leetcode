#Binarysearch.com
#Tempo: O(n), Espaço: O(n)
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
        aux = LLNode(stack.pop(-1))
        result = aux
        while(len(stack) > 0):
            result.next = LLNode(stack.pop(-1))
            result = result.next
        return aux       
        


node1 = LLNode(1)
node2 = LLNode(2)
node3 = LLNode(3)
node4 = LLNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.solve(node1)