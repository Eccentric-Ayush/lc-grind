#Brute force but the more optimized version
def restoreIpAddresses(s):
    n = len(s)
    result = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+2, n):
                p1 = s[:i]
                p2 = s[i:j]
                p3 = s[j:k]
                p4 = s[k:]

                if valid(p1) and valid(p2) and valid(p3) and valid(p4) :
                    result.append(f"{p1}.{p2}.{p3}.{p4}")
    
    return result

def valid(part):
    if len(part) == 0:
        return False
    if len(part) > 1 and part[0] == '0':
        return False

# value check
    if int(part) > 255:
        return False
    
    return True