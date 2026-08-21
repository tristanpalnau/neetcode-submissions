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

        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            if isSameTree(cur, subRoot):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
        
            
            
