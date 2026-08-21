# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            queue = deque([(p, q)])
            while queue:        
                a, b = queue.popleft()
                if not a and not b:
                    continue
                if not a or not b:
                    return False
                if a.val != b.val:
                    return False
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
            return True

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)