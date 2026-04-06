"""
TREE TRAVERSALS (EASY EXPLANATION)

1. What is a Tree Traversal?
----------------------------
In an Array, traversing (exploring) is easy: you literally just run a `for` 
loop from index 0 to the end.

But in a Tree, data branches out in multiple directions! You can't just use 
a basic loop. You have to decide strategically *when* to read the Parent Node, 
*when* to go down the Left Branch, and *when* to go down the Right Branch.

This gives us 3 famous ways to explore ("traverse") a binary tree using Recursion.
The names (In-order, Pre-order, Post-order) simply tell you exactly WHEN you 
should print/read the ROOT (Parent) node!

2. IN-ORDER Traversal (Left -> Root -> Right)
---------------------------------------------
The Rule: Go as far Left as possible, then read the Root, then go Right.
Why use it? 
- If you run an In-Order traversal on a Binary Search Tree (BST), it magically 
  prints every single number in perfectly sorted ascending order!

3. PRE-ORDER Traversal (Root -> Left -> Right)
----------------------------------------------
The Rule: Read the Root FIRST, then go Left, then go Right.
Why use it? 
- It is amazing for making an exact COPY (clone) of a tree! Since you read the 
  parents before the children, you can easily rebuild the exact same top-down structure.

4. POST-ORDER Traversal (Left -> Right -> Root)
-----------------------------------------------
The Rule: Go Left, then go Right, and read the Root LAST!
Why use it? 
- It is perfect for DELETING a tree! You are forced to visit and safely delete 
  all the children *before* you delete their parent. (If you deleted the parent 
  first, you'd lose the pointers to the children and they'd be stuck in memory forever!)
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ==========================================
# --- The 3 Traversals ---
# ==========================================

def in_order(node, result=None):
    """LEFT -> ROOT -> RIGHT"""
    if result is None:
        result = []
        
    if node:
        in_order(node.left, result)     # 1. Look Left
        result.append(node.data)        # 2. Capture Root
        in_order(node.right, result)    # 3. Look Right
    return result


def pre_order(node, result=None):
    """ROOT -> LEFT -> RIGHT"""
    if result is None:
        result = []
        
    if node:
        result.append(node.data)        # 1. Capture Root FIRST!
        pre_order(node.left, result)    # 2. Look Left
        pre_order(node.right, result)   # 3. Look Right
    return result


def post_order(node, result=None):
    """LEFT -> RIGHT -> ROOT"""
    if result is None:
        result = []
        
    if node:
        post_order(node.left, result)   # 1. Look Left
        post_order(node.right, result)  # 2. Look Right
        result.append(node.data)        # 3. Capture Root LAST!
    return result


def demonstrate_traversals():
    r"""
    We will build this exact tree:
           A
         /   \
        B     C
       / \   / \
      D   E F   G
    """
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right.left = TreeNode("F")
    root.right.right = TreeNode("G")
    
    print("--- Tree Traversals Demonstration ---")
    print(f"IN-ORDER (Left, Root, Right):   {in_order(root)}")
    # Expected Output: ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    
    print(f"\nPRE-ORDER (Root, Left, Right):  {pre_order(root)}")
    # Expected Output: ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    
    print(f"\nPOST-ORDER (Left, Right, Root): {post_order(root)}")
    # Expected Output: ['D', 'E', 'B', 'F', 'G', 'C', 'A']

if __name__ == "__main__":
    demonstrate_traversals()
