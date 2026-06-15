# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ll = []
        temp = head
        while temp and temp.next:
            ll.append(temp.val)
            temp = temp.next
        ll.append(temp.val)
        n=len(ll)
        sum = []
        for i in range(0,n//2):
            sum.append(ll[i]+ll[n-1-i])
        return max(sum)