class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        new = []
        for i in nums:
            new.append(abs(i-med))
        return sum(new)