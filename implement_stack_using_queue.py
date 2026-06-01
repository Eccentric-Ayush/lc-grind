#Optimal Solution
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Get the current size before appending
        size = len(self.q)
        
        # Add the new element to the back of the queue
        self.q.append(x)
        
        # Rotate the queue: pull elements from the front 
        # and push them to the back, except for the new element.
        for _ in range(size):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0