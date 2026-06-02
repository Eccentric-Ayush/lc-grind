#Optimized Solution

def lengthOfLongestSubstring(self, s):
    has = set()
    n = []
    left = 0
    for right in range(len(s)):
        while s[right] in has:
            has.remove(s[left])
            left += 1

        has.add(s[right])
        n.append(right - left + 1)
    return max(n) if n else 0