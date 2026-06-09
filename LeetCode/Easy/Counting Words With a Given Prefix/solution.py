class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            check = ''
            for i in word:
                check += i
                if check == pref:
                    count += 1
                    continue
        return count