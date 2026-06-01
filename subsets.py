#Brute Force
def subsets(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output