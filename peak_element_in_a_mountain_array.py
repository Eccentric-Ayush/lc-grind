#Add Optimal Solution
def peakIndexInMountainArray(self, arr):
    low, high = 0, len(arr)-1
    while low<high:
        peak = (low+high)//2
        if arr[peak] < arr[peak+1]:
            low = peak+1
        else:
            high = peak
    return low