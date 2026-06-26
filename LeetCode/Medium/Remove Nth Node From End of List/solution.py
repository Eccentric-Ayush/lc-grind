# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp and temp.next:
            count += 1
            temp = temp.next
        count += 1
        temp = head
        if count!=1 and n==1:
            while temp.next and temp.next.next !=None:
                temp = temp.next
            temp.next= None
            return head
        elif count==1 and n==1:
            return None
        elif count==n:
            return head.next
        else:
            for i in range(count-n-1):
                temp = temp.next
            temp.next = temp.next.next
            return head

