#Brute Force Approach
from collections import Counter
def limitOccurrences(nums, k):
    c = Counter(nums)
    for i in c:
        if c[i]>k:
            while c[i]>k:
                nums.remove(i)
                c[i] -= 1
    return nums