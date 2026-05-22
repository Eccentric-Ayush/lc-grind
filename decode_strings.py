#Optimal Solution
def decodeString(s):
    stack, cur, num = [], '', 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            stack.append((cur, num))
            cur = ''
            num = 0
        elif c == ']':
            prev, n = stack.pop()
            cur = prev + cur * n
        else:
            cur += c
    return cur
