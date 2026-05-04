# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minval, maxval):
            if not node:
                return True
            else:
                if minval <node.val < maxval:
                    return all([dfs(node.left, minval, node.val), dfs(node.right, node.val, maxval)])
                else:
                    return False
        return dfs(root, float('-infinity'), float('infinity'))