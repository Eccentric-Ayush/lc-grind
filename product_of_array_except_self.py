def productExceptSelf(nums):
    n = len(nums)
    res = []
    for i in nums:
        prod = 1
        for j in nums:
            if i!= j:
                prod *= j
            if j==0:
                continue
        res.append(prod)
    return res


