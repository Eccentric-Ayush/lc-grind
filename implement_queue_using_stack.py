#Optimal Solution
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move_elements()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move_elements()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out

    def move_elements(self) -> None:
        """
        Helper function to transfer elements from stack_in to stack_out
        only when stack_out is empty.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())