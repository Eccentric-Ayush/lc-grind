#Optimsed Code
def diffWaysToCompute(expression):
    res = []
    for i, c in enumerate(expression):
        if c in '+-*':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for l in left:
                for r in right:
                    if c == '+':
                        res.append(l + r)
                    elif c == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res or [int(expression)]