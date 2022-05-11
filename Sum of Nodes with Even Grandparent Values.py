#Tempo: O(n), Espaço:O(n) Usado pela stack
class Tree:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def dfs(self,root:Tree,parent,grandParent):
        value = 0
        if(root == None):
            return 0 
        if(grandParent != None and grandParent % 2 == 0):
            value = root.val
        grandParent = parent
        parent = root.val
        sumN = self.dfs(root.left,parent,grandParent) + self.dfs(root.right,parent,grandParent) + value
        return sumN

    def solve(self, root):
        sumN = self.dfs(root,None,None)
        return sumN