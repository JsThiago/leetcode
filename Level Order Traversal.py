from unittest import result


class Tree:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def bfs(self:Tree,stack:list):
        queue = []
        while(len(stack)>0):
            actual:Tree = stack.pop()
            queue.append(actual.val)
            if(actual.left != None):
                stack.insert(0,actual.left)
            if(actual.right != None):
                stack.insert(0,actual.right) 
        return queue
        
        
    def solve(self, root):
        queue = self.bfs([root])
        return queue


root = Tree(0)
node1 = Tree(5)
node2 = Tree(9)
node3 = Tree(1)
node4 = Tree(3)
node5 = Tree(4)
node6 = Tree(2)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6
solution = Solution()
solution.solve(root)