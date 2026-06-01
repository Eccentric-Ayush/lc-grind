#Brute Force
from collections import Counter
def countWords(words1, words2):
    w1 = Counter(words1)
    lst = []
    for i, j in w1.items():
        if j==1:
            lst.append(i)
    
    w2 = Counter(words2)
    lst2 = []
    for i, j in w2.items():
        if j==1:
            lst2.append(i)
    count = 0
    for i in lst:
        if i in set(lst2):
            count += 1
    return count
    