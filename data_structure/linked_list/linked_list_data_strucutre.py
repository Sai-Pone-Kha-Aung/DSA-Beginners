"""
LINKED LIST DATA STRUCTURE

1. What is a Linked List?
-------------------------
A Linked List is a linear data structure, but unlike an array, its elements 
are NOT stored in contiguous (adjacent) locations in memory. 
Instead, each element is a completely separate object scattered in memory, 
called a "Node".

2. Structure of a Node:
-----------------------
Every Node contains two parts:
- Data: The actual value being stored.
- Next Pointer: A reference (or link) to the next node in the sequence.

The very first node is called the 'Head', and the very last node points to 'None',
signaling the absolute end of the list.

3. Why use Linked Lists instead of Arrays?
------------------------------------------
Advantages:
- Dynamic Size: They can grow and shrink in memory seamlessly without 
  needing to be resized, copied, or reallocated like static arrays.
- Insertions/Deletions: Adding or removing an element at the beginning 
  or middle is extremely fast O(1), provided you have the pointer to that
  location. This is because you don't need to shift any neighboring elements 
  over to make room!

Disadvantages:
- No Random Access: You cannot jump directly to a specific index like `arr[3]`.
  You must traverse the list one-by-one from the Head node to find your desired 
  element O(n).
- Extra Memory: Each element requires extra memory to store the 'Next' pointer.

4. Time Complexities:
---------------------
- Access by index: O(n)
- Search for a value: O(n)
- Insertion (at Head): O(1)
- Insertion (at Tail): O(n) (or O(1) if you maintain a separate Tail pointer)
- Deletion (at Head): O(1)
"""

# ==========================================
# --- Linked List Implementation ---
# ==========================================

class Node:
    """A Node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    """A Singly Linked List."""
    def __init__(self):
        self.head = None  # Starts completely empty
        
    def append(self, data):
        """Adds a new node to the end (Tail) of the list."""
        new_node = Node(data)
        
        # If the list is completely empty, the new node becomes our Head
        if self.head is None:
            self.head = new_node
            return
            
        # Otherwise, traverse to the very end of the list
        current = self.head
        while current.next:
            current = current.next
            
        # Point the last node's 'next' to our new node
        current.next = new_node
        
    def prepend(self, data):
        """Adds a new node to the beginning (Head) of the list. O(1) time!"""
        new_node = Node(data)
        # Point the new node's 'next' to the current Head
        new_node.next = self.head
        # Update our list's Head to be the new node
        self.head = new_node
        
    def delete_with_value(self, data):
        """Finds and deletes the first node with the specified data."""
        if self.head is None:
            return
            
        # If the head is the exact node to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return
            
        # Traverse looking for the node, keeping track of the previous node
        current = self.head
        while current.next:
            if current.next.data == data:
                # Found it! Skip over the node we want to delete perfectly
                current.next = current.next.next
                return
            current = current.next
            
    def display(self):
        """Returns the list as a readable string for printing."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"


if __name__ == "__main__":
    print("--- Linked List Demonstration ---")
    
    # 1. Initialize
    my_list = LinkedList()
    print(f"Empty list: {my_list.display()}")
    
    # 2. Append elements
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print(f"\nAfter appending 10, 20, 30:\n{my_list.display()}")
    
    # 3. Prepend an element (O(1) insertion)
    my_list.prepend(5)
    print(f"\nAfter prepending 5 at the Head:\n{my_list.display()}")
    
    # 4. Delete an element from the middle
    my_list.delete_with_value(20)
    print(f"\nAfter deleting 20:\n{my_list.display()}")
