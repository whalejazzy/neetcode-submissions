# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxval, minval):
            if not node:
                return True
            
            if node.val >= maxval or node.val <= minval:
                return False

            return all([dfs(node.left, node.val, minval), dfs(node.right, maxval, node.val)])
        return dfs(root, 1001, -1001)
        





    #             1
    #     0               3
    # -2      0.5     2       5
