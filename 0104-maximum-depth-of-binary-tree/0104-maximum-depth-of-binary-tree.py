# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(current):
            if current is None:
                return 1
            elif (current.left == None and current.right == None):
                return 1
            
            return 1 + max(dfs(current.left), dfs(current.right))
        
        return dfs(root)