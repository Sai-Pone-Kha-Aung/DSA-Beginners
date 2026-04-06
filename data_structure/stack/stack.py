class Stack:
    """A simple implementation of a Stack data structure using a Python list."""
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        """Check if the stack is empty.
        Returns True if empty, False otherwise.
        """
        return len(self.items) == 0
        
    def push(self, item):
        """Add an item to the top of the stack.
        Time Complexity: O(1) amortized
        """
        self.items.append(item)
        
    def pop(self):
        """Remove and return the item from the top of the stack.
        Returns None if the stack is empty (or raises an Exception).
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None # Alternative: raise IndexError("pop from empty stack")
        return self.items.pop()
        
    def peek(self):
        """Return the top item from the stack without removing it.
        Returns None if the stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None # Alternative: raise IndexError("peek from empty stack")
        return self.items[-1]
        
    def size(self):
        """Return the number of items in the stack.
        Time Complexity: O(1)
        """
        return len(self.items)

    def __str__(self):
        """String representation of the stack for printing."""
        return str(self.items)

# Example usage:
if __name__ == "__main__":
    s = Stack()
    print("Is empty?", s.is_empty())  # True
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushes:", s)   # [10, 20, 30]
    print("Top item (peek):", s.peek()) # 30
    print("Popped item:", s.pop())      # 30
    print("Stack after pop:", s)        # [10, 20]
    print("Size:", s.size())            # 2
