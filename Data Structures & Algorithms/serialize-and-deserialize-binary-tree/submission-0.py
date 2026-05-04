# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.out = ""
        if root is None:
            return ""
        def dfs(node):
            if not node:
                self.out += "N,"
                return
            else:
                self.out += str(node.val) + ","
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.out
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = 0
        def dfs(l):
            if l == len(data):
                return None, l
            r = l
            print(type(r))
            while data[r] != ",":
                r+= 1
            if data[l:r] == "N":
                return None, r+1
            node = TreeNode(int(data[l:r]))
            node.left, idx = dfs(r+1)
            node.right, idx = dfs(idx)
            return node, idx
        root,_ = dfs(0)
        return root