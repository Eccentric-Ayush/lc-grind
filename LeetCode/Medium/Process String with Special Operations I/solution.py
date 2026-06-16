class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for i in s:
            if i=='*':
                stack.pop() if stack else '#'
            elif i=='#':
                stack += stack
            elif i=='%':
                stack = stack[::-1]
            else:
                stack.append(i)
        return ''.join(stack)