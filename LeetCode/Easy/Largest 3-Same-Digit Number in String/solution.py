from collections import Counter

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nos = []
        c = Counter(num)
        
        for i in c.keys():
            if c[i] > 2:
                if (i * 3) in num:
                    nos.append(int(i))
        if nos:
            return str(max(nos)) * 3
        else:
            return ""