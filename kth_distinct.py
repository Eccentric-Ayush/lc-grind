from collections import Counter
def kthDistinct(arr, k):
    a1 = Counter(arr)
    lst = []
    for j,i in a1.items():
        if i==1:
            lst.append(j)
    return lst[k-1] if k<= len(lst) else ""
