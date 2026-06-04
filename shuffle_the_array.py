class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1 = nums[:n]
        num2 = nums[n:]
        res = []
        
        # Loop n times to grab one element from each half
        for i in range(n):
            res.append(num1[i])
            res.append(num2[i])
            
        return res