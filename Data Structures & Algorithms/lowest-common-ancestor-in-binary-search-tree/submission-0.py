# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([(root, [root])])
        nodes = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node,ancestors = queue.pop()
                if node.val == p.val or node.val == q.val:
                    nodes.append(ancestors)
                if node.left:
                    queue.appendleft((node.left, ancestors + [node.left]))
                if node.right:
                    queue.appendleft((node.right, ancestors + [node.right]))    
            if len(nodes) == 2:
                break
        print([n.val for n in nodes[0]])
        print([n.val for n in nodes[1]])
        while nodes[0][-1] != nodes[1][-1]:
            if len(nodes[0]) > len(nodes[1]):
                nodes[0].pop()
            else:    
                nodes[1].pop()
        return nodes[0][-1]
                
            