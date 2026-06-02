#Optimized Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        str1 = ''
        temp = l1
        while temp.next != None:
            str1 += str(temp.val)
            temp = temp.next
        str1 += str(temp.val)
        str2 = ''
        temp = l2
        while temp.next != None:
            str2 += str(temp.val)
            temp = temp.next
        str2 += str(temp.val)
        str1 = str1[::-1]
        str2 = str2[::-1]
        str3 = str(int(str1)+int(str2))[::-1]
        dummy = ListNode(0)
        temp = dummy
        for i in str3:
            temp.next = ListNode(int(i))
            temp = temp.next
        
        return dummy.next
            

        