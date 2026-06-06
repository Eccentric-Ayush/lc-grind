#Brute Force Approach
def minAbsoluteDifference(nums):
    min_diff = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i]==1 and nums[j]==2:
                min_diff = min(min_diff, abs(i-j))
            elif nums[i]==2 and nums[j]==1:
                min_diff = min(min_diff, abs(i-j))
    return min_diff if min_diff!= float('inf') else -1
