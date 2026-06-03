class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        x = nums1 + nums2
        y = sorted(x)
        h = int(len(y)//2)
        if len(y)%2!=0:
            return y[h]
        else:
            f = (y[h] +y[h-1]) /2
            return f

        