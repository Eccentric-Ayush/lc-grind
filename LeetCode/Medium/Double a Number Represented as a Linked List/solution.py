import sys

# Increase the string-to-integer conversion limit safely
sys.set_int_max_str_digits(10000)

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Build the string from the linked list
        temp = head
        st = ''
        while temp:
            st += str(temp.val)
            temp = temp.next
            
        # 2. Math: Double the number (This won't crash anymore!)
        st = int(st) * 2
        st = str(st)
        
        # 3. Rebuild the linked list using the digits
        dummy = ListNode(0)
        current = dummy
        
        for digit in st:
            current.next = ListNode(int(digit))
            current = current.next
            
        return dummy.next