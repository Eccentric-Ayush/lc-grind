#Optimized Solution
def topKFrequent(nums, k):
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    unique = list(hash_map.keys())
    unique.sort(key = lambda x: hash_map[x], reverse = True)
    return unique[:k]