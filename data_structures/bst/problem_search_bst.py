"""
PROBLEM: Search in a Binary Search Tree (EASY)

Description:
You are given the `root` Node of a standard Binary Search Tree (BST) 
and a specific integer `target`.

You must find the exact Node inside the BST that the given `target` 
matches and return True. If the `target` does not exist inside the BST, 
simply return False.

Example 1:
Input: root = [4,2,7,1,3], target = 2
Output: True

Example 2:
Input: root = [4,2,7,1,3], target = 5
Output: False

Hint:
Use the classic Recursion structure, and remember the Golden Rule of the BST:
If the `target` is SMALLER than the current Node's data... immediately 
throw away the entire Right half of the tree, and ONLY search the Left half!

If the `target` is LARGER than the current Node's data... immediately 
throw away the Left half of the tree, and ONLY search the Right half!
"""

class TreeNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def searchBST(root, target):
    """
    Hunts for the target utilizing the BST rule!
    
    :param root: TreeNode
    :param target: int
    :return: True or False
    """
    # 1. TODO: Write your Base Cases!
    # (If `root` is None, what do we return? If `root.data` matches the target, what do we return?)
    # if root is None:
    #     return False

    # if root.node == target:
    #     return True
    # # 2. TODO: If `target` is SMALLER than current Node, go Left!
    # if target < root.node:
    #     return searchBST(root.left, target)
    
    # # 3. TODO: If `target` is LARGER than current Node, go Right!
    # if target > root.node:
    #     return searchBST(root.right, target)
    current = root 

    while current is not None:
        if target == current.node:
            return True
        elif target < current.node:
            current = current.left
        else:
            current = current.right
    
    return False


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
def build_bst():
    """Builds a test BST:
          4
        /   \
       2     7
      / \
     1   3
    """
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root

if __name__ == "__main__":
    test_cases = [
        (2, True),    # Search for 2
        (1, True),    # Search for 1
        (7, True),    # Search for 7
        (10, False),  # 10 is missing
        (0, False)    # 0 is missing
    ]
    
    root = build_bst()
    
    all_passed = True
    print("--- Testing BST Search ---")
    for target, expected in test_cases:
        try:
            result = searchBST(root, target)
            found = True if result else False
            
            if found == expected:
                print(f"✅ PASS: Search({target}) -> Returned {found}")
            else:
                print(f"❌ FAIL: Search({target}) -> Expected {expected}, got {found}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: Search({target}) threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
