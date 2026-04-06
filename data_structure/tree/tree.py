"""
TREE DATA STRUCTURE (EASY EXPLANATION)

1. What is a Tree?
------------------
If Arrays and Linked Lists are like a completely straight, single-file line 
of people (Linear Data)...
A Tree is exactly like a massive biological Family Tree (Non-Linear Data)! 

Instead of one item naturally pointing strictly to the *next* item, one core item 
(the "Parent") structurally branches out and aggressively points to multiple 
other distinct items beneath it (the "Children").

Those children then powerfully branch out and violently point to *their* own 
children, rapidly creating a massive, heavily interconnected cascading hierarchy.

2. Important Tree Terminology:
------------------------------
- Node: A predictably single, specific data point inside the Tree (like one person inside a Family Tree).
- Root Node: The absolute very top, undisputed starting Node of the entire tree! (It aggressively has NO parents above it).
- Leaf Nodes: The absolute bottom Nodes of the tree. They are the devastating end of the line. (They have NO children beneath them).
- Edge / Branch: The actual physical connective pointer between a Parent Node and a Child Node.
- Subtree: Because of Recursion, if you look at literally any random Node buried deep in the tree... that Node and all of its descendants legally seamlessly form their very own smaller, mathematically sound "Subtree"!

3. Why do we heavily use Trees?
-------------------------------
Imagine actively organizing folders beautifully on your computer hard drive!
You don't mechanically shove all 100,000 files violently into one wildly giant Array (a massive single flat line).
You logically intuitively use a hierarchical Tree structure:
Root (C: Drive) -> "Users" Folder -> "Alice" Folder -> "Documents" -> "Resume.pdf".

Because data is smartly organized hierarchically into heavily splitting branches, 
you can brutally find exactly what you are looking for phenomenally faster than 
reading a flat, single-file list!

4. The Famous "Binary Tree":
----------------------------
A standard generic Tree can famously have as many children per Parent as it creatively 
wants (like an infinitely chaotic folder with 100 random sub-folders inside).

However, the absolute most mathematically famous concept in all of computer science 
is strictly the **Binary Tree**.
A Binary Tree aggressively enforces ONE critical, legally strict mathematical rule: 
EVERY single Parent Node is physically securely ONLY allowed to have an absolute 
maximum of **TWO** children! (Specifically strictly named the `left` child, and the `right` child).
"""

# ==========================================
# --- Basic Binary Tree Implementation ---
# ==========================================

class TreeNode:
    """A single isolated Node specifically designed for a massive Binary Tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None   # Formal pointer strictly to the Left child
        self.right = None  # Formal pointer strictly to the Right child

def demonstrate_tree():
    print("--- 1. Building a Basic Corporate Binary Tree ---")
    
    # 1. Create the absolute Root Node
    root = TreeNode("CEO (Root Node)")
    
    # 2. Create its powerful immediate Level 2 children
    root.left = TreeNode("VP of Sales (Left Child)")
    root.right = TreeNode("VP of Engineering (Right Child)")
    
    # 3. Aggressively add pure leaf nodes to the very bottom Level 3!
    root.left.left = TreeNode("Sales Manager (Leaf Node)")
    root.right.left = TreeNode("Senior Engineer (Leaf Node)")
    root.right.right = TreeNode("Junior Engineer (Leaf Node)")
    
    print(f"✅ Securely built a Tree! The absolute Root is: '{root.data}'")
    print(f"✅ The Root's Left Child structurally manages Sales: '{root.left.data}'")
    print(f"✅ The Root's Right Child heavily manages Engineering: '{root.right.data}'")
    print(f"✅ The VP of Engineering safely visually manages a heavily buried child node: '{root.right.right.data}'")

if __name__ == "__main__":
    demonstrate_tree()
