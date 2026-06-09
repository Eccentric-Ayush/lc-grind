class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if min(nums1) in set(nums2):
            return min(nums1)
        nums1.sort()
        for i in nums1:
            if i in nums2:
                return i
        if min(nums1)<min(nums2):
            return min(nums1)*10+min(nums2)
        else:
            return min(nums2)*10+min(nums1)