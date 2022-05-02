# Tempo: O(n), Espaço:O(n)
class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node:LLNode):
        aux = node
        array = []
        while(aux != None):
            array.append(aux.val)
            aux = aux.next
        start = 0
        end = len(array) - 1
        while(start <= end):
            if(array[start] != array[end]):
                return False
            start = start + 1
            end = end - 1
        return True

node1 = LLNode(5)
node2 = LLNode(3)
node3 = LLNode(5)
node1.next = node2
node2.next = node3
solution = Solution()
print(solution.solve(node1))