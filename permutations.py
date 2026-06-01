#Hardcore Brute Force Only for the constraints: (1<=n<=6)
def permute(nums):
    result = []
    n = len(nums)

    if n == 1:
        for a in nums:
            result.append([a])

    elif n == 2:
        for a in nums:
            for b in nums:
                if a != b:
                    result.append([a, b])

    elif n == 3:
        for a in nums:
            for b in nums:
                for c in nums:
                    if a != b and b != c and a != c:
                        result.append([a, b, c])

    elif n == 4:
        for a in nums:
            for b in nums:
                for c in nums:
                    for d in nums:
                        if len({a, b, c, d}) == 4:
                            result.append([a, b, c, d])

    elif n == 5:
        for a in nums:
            for b in nums:
                for c in nums:
                    for d in nums:
                        for e in nums:
                            if len({a, b, c, d, e}) == 5:
                                result.append([a, b, c, d, e])

    elif n == 6:
        for a in nums:
            for b in nums:
                for c in nums:
                    for d in nums:
                        for e in nums:
                            for f in nums:
                                if len({a, b, c, d, e, f}) == 6:
                                    result.append([a, b, c, d, e, f])

    return result