from collections import Counter
def kthDistinct(arr, k):
    a1 = Counter(arr)
    # new = dict(sorted(a1.items()))
    # lst = []
    # for i in list(new.keys()):
    #     lst.append(i)
    # # lst = lst[::-1]
    # return lst[k-1] if k<=len(lst) else ""
    lst = []
    for j,i in a1.items():
        if i==1:
            lst.append(j)
    return lst[k-1] if k<= len(lst) else ""
