#Tempo: O(n), Espaço: O(1)

class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node:LLNode, k):
        aux2 = node
        aux = node
        count = 0
        while(True):
            if(count == k):
                aux = aux.next
            if(aux2.next is None):
                break
            aux2 = aux2.next
            count = count + 1            
            
        return aux.val
       
solution = Solution()
node1 = LLNode(0)
node2 = LLNode(1)
node3 = LLNode(2)
node4 = LLNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
solution.solve(node1,2)