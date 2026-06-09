class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if len(word) > len(s):
                continue
                
            ind = 0
            is_prefix = True
            
            for i in word:
                if i == s[ind]:
                    ind += 1
                else:
                    is_prefix = False
                    break
            if is_prefix:
                count += 1
                
        return count