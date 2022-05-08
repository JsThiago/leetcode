class LLNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def solve(self, node:LLNode):
        p1:LLNode = node
        count = 0
        p2:LLNode = p1
        while p1 != None:
            if(count == 1):
                aux = p2.val
                p2.val = p1.val
                p1.val = aux
                count = 0
                p2 = p1.next
                p1 = p1.next
                if(p1 == None):
                    break
            p1 = p1.next
            count = count + 1
        return node


node = LLNode(1)
node1 = LLNode(2)
node2 = LLNode(3)
node.next = node1
node1.next = node2

solution = Solution()
solution.solve(node)