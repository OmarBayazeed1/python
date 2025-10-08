#111.Implement a stack using a list
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add the item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the item from the top."""
        try:
            return self.stack.pop()
        except IndexError:
            print("Cannot pop, stack is empty!")
            return None
        

    def peek(self):
        """Return the item at the top without removing it."""
        try:
            return self.stack[-1]
        except IndexError:
            print("Cannot peek, stack is empty!")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.stack)
m=MyStack()
m.pop()
m.push(10)
print(m.__str__())
