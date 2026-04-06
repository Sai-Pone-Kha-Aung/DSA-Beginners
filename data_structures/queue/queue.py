from collections import deque

class Queue:
    """A simple implementation of a Queue data structure using collections.deque."""
    
    def __init__(self):
        # We use a deque instead of a list because inserting/removing from the 
        # beginning of a list takes O(n) time, whereas deque has O(1) operations.
        self.items = deque()
        
    def is_empty(self):
        """Check if the queue is empty.
        Returns True if empty, False otherwise.
        """
        return len(self.items) == 0
        
    def enqueue(self, item):
        """Add an item to the back of the queue.
        Time Complexity: O(1)
        """
        self.items.append(item)
        
    def dequeue(self):
        """Remove and return the item from the front of the queue.
        Returns None if the queue is empty (or raises an Exception).
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None # Alternative: raise IndexError("dequeue from empty queue")
        return self.items.popleft()
        
    def peek(self):
        """Return the front item from the queue without removing it.
        Returns None if the queue is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None # Alternative: raise IndexError("peek from empty queue")
        return self.items[0]
        
    def size(self):
        """Return the number of items in the queue.
        Time Complexity: O(1)
        """
        return len(self.items)

    def __str__(self):
        """String representation of the queue for printing."""
        return str(list(self.items))

# Example usage:
if __name__ == "__main__":
    q = Queue()
    print("Is empty?", q.is_empty())  # True
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("Queue after enqueues:", q) # ['A', 'B', 'C']
    print("Front item (peek):", q.peek()) # 'A'
    print("Dequeued item:", q.dequeue())  # 'A'
    print("Queue after dequeue:", q)      # ['B', 'C']
    print("Size:", q.size())              # 2
