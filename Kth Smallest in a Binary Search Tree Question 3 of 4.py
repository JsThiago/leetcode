class Tree:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self,node:Tree,array:list):
        if(node == None):
            return
        if(node.left != None):
            array.append(node.left)
            self.dfs(node.left,array)
        if(node.right != None):
            array.append(node.right,array)
            self.dfs(node.right,array)
    def solve(self, root, k):
        array = []
        self.dfs(root,array)
        print(array)

solution = Solution()
root = Tree(3)
node1 = Tree(2)
node2 = Tree(9)
node3 = Tree()

        