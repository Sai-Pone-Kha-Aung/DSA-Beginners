"""
PROBLEM: Find the Middle Node of a Linked List

Description:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes (i.e., the list has an even number of elements), 
return the second middle node.

Constraint:
Try to do this in ONE single pass through the linked list!
(Hint: Think about using two pointers, one moving twice as fast as the other. 
When the fast pointer reaches the end, where will the slow pointer be?)

Example 1:
Input List: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output Node Data: 3

Example 2:
Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
Output Node Data: 4

Example 3:
Input List: 42 -> None
Output Node Data: 42
"""

class Node:
    """A Node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle_node(head):
    """
    Finds and returns the middle node of the linked list.
    
    :param head: Node (the head of the linked list)
    :return: Node (return the actual Node object, not just the data!)
    """
    # TODO: Implement your solution here!
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow




# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
def build_linked_list(elements):
    """Helper to build a linked list from an array."""
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for el in elements[1:]:
        current.next = Node(el)
        current = current.next
    return head

def get_node_data(node):
    """Helper to safely extract data from a node for testing."""
    return node.data if node else None

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
        ([42], 42),
        ([10, 20], 20),
        ([], None)
    ]
    
    all_passed = True
    for arr, expected in test_cases:
        head = build_linked_list(arr)
        result_node = find_middle_node(head)
        result_data = get_node_data(result_node)
        
        if result_data == expected:
            print(f"✅ PASS: List {arr} -> Middle is {result_data}")
        else:
            print(f"❌ FAIL: List {arr} -> Expected {expected}, got {result_data}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
