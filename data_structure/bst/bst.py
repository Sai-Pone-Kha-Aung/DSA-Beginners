"""
BINARY SEARCH TREE (BST) - (EASY EXPLANATION)

1. What is a Binary Search Tree (BST)?
--------------------------------------
You literally just learned about a normal "Binary Tree" (where every Parent Node 
can legally have up to 2 random children). 

A Binary SEARCH Tree is an extremely special, incredibly mathematically powerful 
version of a Binary Tree that violently enforces ONE massive additional structural rule:

Everything to the LEFT of a Node must logically be strictly SMALLER than it.
Everything to the RIGHT of a Node must structurally be strictly LARGER than it.

2. Why is this rule so incredibly powerful?
-------------------------------------------
Imagine you are desperately looking for the number 10,000 in a massive Tree 
with millions of complex Nodes.

You start at the absolute very top (the Root Node). The Root Node mysteriously 
happens to be the number 50,000.
Because of the Golden BST Rule, you INSTANTLY mathematically securely know that 
10,000 is heavily smaller than 50,000. Therefore, the number 10,000 physically 
MUST be somewhere completely exclusively down the Left Branch!

You can completely blindly bravely throw away the entire massive, intricate Right 
Branch (which could violently contain half a million nodes!) without having to 
check a single one of them.
Every single step you take safely down the tree, you magically chop your search 
time IN HALF! (Does this conceptually sound familiar? It is structurally literally 
the visual Tree version of Binary Search!)

3. Time Complexities:
---------------------
- Best / Average Case: O(log n) -> Because you aggressively legally eliminate 
  exactly 50% of the tree at every branching junction, you can search 1,000,000 
  items in just ~20 blazing fast steps! (Inserting, Searching, and Deleting all 
  securely take a mere O(log n) time!).

- Worst Case: O(n) -> Imagine if you accidentally insert perfectly sorted numbers 
  into your tree in order: 1, then 2, then 3, then 4, then 5. 
  Every single number will legally mathematically be placed exclusively onto the 
  Right Branch of the previous number! 
  You just accidentally built a massive, visually slanted straight line... which 
  is functionally just a terribly slow Linked List! You totally lose all the magical 
  "chopping in half" superpowers and have to literally explicitly search them 
  painfully one-by-one (O(n)).

4. Important Tree Traversals:
-----------------------------
How do you systematically successfully print out every Node deeply buried in a tree?
- In-Order Traversal: Visits Left -> Root -> Right. (Massive Secret: In a BST, 
  this miraculously intelligently prints every single incredibly jumbled inserted 
  Node perfectly in ascending numerical order!)
- Pre-Order Traversal: Visits Root -> Left -> Right.
- Post-Order Traversal: Visits Left -> Right -> Root.
"""

# ==========================================
# --- Binary Search Tree Implementation ---
# ==========================================

class TreeNode:
    """A single isolated Node specifically beautifully designed for a massive BST."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """The master controller visually wrapping the hierarchical structure."""
    def __init__(self):
        self.root = None  # The tree bravely starts completely perfectly empty

    def insert(self, data):
        """Safely violently injects a shiny new piece of data deep into the legal Tree."""
        if self.root is None:
            self.root = TreeNode(data)  # Becomes the absolute King!
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, current_node, data):
        """Actively mathematically gracefully recursively hunts for the perfectly legal empty spot."""
        # Is the data heavily SMALLER? Forcefully bravely go Left!
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data) # Found an empty slot! Drop it flawlessly!
            else:
                self._insert_recursive(current_node.left, data) # Keep fiercely walking left...
                
        # Is the data heavily LARGER? Safely confidently go Right!
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data) # Found an empty slot! Drop it fiercely!
            else:
                self._insert_recursive(current_node.right, data) # Keep aggressively walking right...

    def search(self, data):
        """Blisteringly quickly accurately recursively hunts for a value in O(log n) time."""
        return self._search_recursive(self.root, data)
        
    def _search_recursive(self, current_node, data):
        # BASE CASES: We mathematically safely hit the bottom brick wall (None), or we impressively found it!
        if current_node is None:
            return False
            
        if current_node.data == data:
            return True
            
        # Is the data mathematically smaller? Heavily aggressively explicitly throw away the Right side and confidently look Left!
        if data < current_node.data:
            return self._search_recursive(current_node.left, data)
            
        # Is the data mathematically bigger? Beautifully aggressively exclusively throw away the Left side and faithfully look Right!
        return self._search_recursive(current_node.right, data)

    def in_order_traversal(self, current_node, result=None):
        """Miraculously beautifully recursively prints the wildly organically branched BST perfectly in ascending numerical order!"""
        if result is None:
            result = []
            
        if current_node:
            self.in_order_traversal(current_node.left, result)  # Go all the way incredibly fiercely Left
            result.append(current_node.data)                    # Capture the Root (perfect center action)
            self.in_order_traversal(current_node.right, result) # Go all the way violently securely Right
            
        return result


def demonstrate_bst():
    print("--- 1. Building a Fast Binary Search Tree ---")
    bst = BinarySearchTree()
    
    # 1. Let's physically authentically insert completely random, aggressively scrambled numbers wildly
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
        
    print("✅ Successfully elegantly built a beautifully mathematically accurately arranged BST!")
    
    # 2. Test the famous In-Order Traversal
    print(f"\n✅ In-Order Traversal (Notice it explicitly prints perfectly sorted!): \n   {bst.in_order_traversal(bst.root)}")
    
    # 3. Test lightning-fast O(log n) Searching
    print("\n✅ Actively beautifully Searching for 40: ", bst.search(40))
    print("❌ Actively fiercely Searching for 99 (Does not exist anywhere): ", bst.search(99))


if __name__ == "__main__":
    demonstrate_bst()
