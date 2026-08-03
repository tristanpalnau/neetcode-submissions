class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"]": "[", ")": "(", "}": "{"}
        stack = []

        for r in s:
            if r in pairs:
                if not stack or stack[-1] != pairs[r]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(r)
            
        return False if stack else True