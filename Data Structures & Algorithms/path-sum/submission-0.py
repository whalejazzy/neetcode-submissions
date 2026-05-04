# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, curr):
            if not node:
                return False
            curr += node.val
            if not node.left and not node.right and curr == targetSum:
                return True
            if backtrack(node.left, curr) or backtrack(node.right, curr):
                return True
            return False
        return backtrack(root, 0)
            