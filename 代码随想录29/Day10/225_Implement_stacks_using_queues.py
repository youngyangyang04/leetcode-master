from collections import deque


class MyStack:
    def __init__(self):
        """
        'que' is used as the underlying data structure for the stack.
        """
        self.que = deque()

    def push(self, x: int) -> None:
        """
        Pushes the element 'x' onto the stack.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes and returns the element from the top of the stack.
        """
        if self.empty():
            return None
        # Rotate the elements in the queue to bring the front element to the back.
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        """
        Returns the element at the top of the stack without removing it.
        """
        if self.empty():
            return None
        # Rotate the elements in the queue to bring the front element to the back.
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.
        """
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
