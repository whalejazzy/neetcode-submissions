# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root, subroot):
            if not root and not subroot:
                return True
            if (root and not subroot) or (not root and subroot) or root.val != subroot.val:
                return False
            return same(root.left, subroot.left) and same(root.right, subroot.right)
        
        if not subRoot:
            return True
        if not root:
            return False
        return any([same(root,subRoot), self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)])