#Brute Force
def subsetsWithDup(nums):
    nums.sort()
    result = [[]]
    i = 0
    while i < len(nums):
        count = 1
        while i + count < len(nums) and nums[i+count]==nums[i]:
            count += 1
        new = []
        for subset in result:
            for c in range(1, count+1):
                new.append(subset+[nums[i]]*c)
        result += new
        i += count
    return result
            