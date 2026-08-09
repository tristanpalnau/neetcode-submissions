class Solution:
    def isValid(self, s: str) -> bool:
        key = {")": "(", "}": "{", "]": "["}
        stack = []
        for _ in s:
            if _ not in key:
                stack.append(_)
            elif _ in key and not stack or _ in key and stack[-1] != key[_]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True