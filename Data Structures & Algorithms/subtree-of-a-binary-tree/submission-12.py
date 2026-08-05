# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        stack = [root]
        while stack:
            p = stack.pop()
            if isSameTree(p, subRoot):
                return True
            else:
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
        return False
