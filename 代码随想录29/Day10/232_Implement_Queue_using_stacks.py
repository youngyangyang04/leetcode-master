class MyQueue:
    def __init__(self):
        """
        'stack_in' is primarily responsible for 'push', and 'stack_out' is primarily responsible for 'pop'.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        When a new element arrives, push it into 'stack_in'.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns that element.
        """
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            # Transfer elements from 'stack_in' to 'stack_out' for popping in the correct order.
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element without removing it.
        """
        # Peek at the front element by calling 'pop' and then restoring it.
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        The queue is empty if both 'stack_in' and 'stack_out' have no elements.
        """
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
