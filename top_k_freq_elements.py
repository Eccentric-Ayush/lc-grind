#Optimized Solution
def topKFrequent(nums, k):
    h = {}
    for i in nums:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1
    unique = list(h.keys())
    unique.sort(key = lambda x: h[x], reverse = True)
    return unique[:k]