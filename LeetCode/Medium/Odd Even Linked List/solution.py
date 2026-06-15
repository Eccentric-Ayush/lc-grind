class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        
        # Create dummy heads to anchor the lists
        odd_dummy = ListNode(None)
        even_dummy = ListNode(None)
        
        # Use runner pointers to build the lists
        odd = odd_dummy
        even = even_dummy
        
        count = 1
        
        # Traverse through every single node
        while temp:
            if count % 2 != 0:
                odd.next = ListNode(temp.val)  # Create a new node with the value
                odd = odd.next                 # Move the runner forward
            else:
                even.next = ListNode(temp.val) # Create a new node with the value
                even = even.next                # Move the runner forward
            
            count += 1
            temp = temp.next
        
        # Stitch the odd list and even list together
        # odd_dummy.next is the start of odds; even_dummy.next is the start of evens
        odd.next = even_dummy.next
        
        return odd_dummy.next