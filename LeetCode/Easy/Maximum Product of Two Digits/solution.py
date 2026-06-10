class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        for i in str(n):
            arr.append(int(i))
        arr = sorted(arr)
        arr =arr[::-1]
        return arr[0]*arr[1]