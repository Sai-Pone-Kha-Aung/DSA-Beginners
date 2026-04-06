"""
PROBLEM: Find if Path Exists in Graph

Description:
There is a bi-directional graph with 'n' vertices. You are given the Graph 
(represented as an Adjacency List / Python Dictionary).
You also receive a `source` node and a `destination` node.

Return `True` if there is ANY valid path that leads entirely from the `source` 
to the `destination`. Return `False` if no path exists.

Example 1:
Input: source = "A", destination = "C"
Graph: {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
Output: True (You can step directly from A to C)

Example 2:
Input: source = "A", destination = "Z"
Graph: {"A": ["B"], "B": ["A"], "Z": []}
Output: False (There is no connecting line to Z)

Hint:
DFS is exceptionally good at finding paths! If you just run a standard 
recursive DFS starting at the `source` node, you can simply check if 
the `destination` node ever organically appears in your `visited` set!
"""

def validPath(graph, source, destination, visited=None):
    """
    Uses Recursion (DFS) to find if a path exists between two nodes.
    
    :param graph: dict
    :param source: str
    :param destination: str
    :param visited: set
    :return: bool
    """
    # 1. Initialize the Visited Set on the very first recursive call!
        # TODO: Create a brand new Set!
    if visited is None:
        visited = set()
        
    # 2. Add the current `source` node to your Visited Set so we don't loop forever!
    visited.add(source)
    # 3. BASE CASE: Did we successfully reach the destination?
    # If source == destination: Return True!
    if source == destination:
        return True
    
    # 4. RECURSIVE CASE: Look at all the neighbors of this exact `source` node
    # For every neighbor in graph[source]:
        # If the neighbor is NOT in the visited set:
            # Recursively call `validPath` again! 
            # (If that recursive call returns True, immediately return True!)
    for neighbour in graph[source]:
        if neighbour not in visited:
            if validPath(graph, neighbour, destination, visited):
                return True

    # 5. If we check every possible hallway and never find it, return False.
    return False

# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================

test_graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C", "F"],
    "F": ["E"],
    "X": ["Y"],       # X and Y are completely disconnected from the rest!
    "Y": ["X"]
}

if __name__ == "__main__":
    test_cases = [
        ("A", "A", True),  # Trivial: Already there
        ("A", "B", True),  # Direct connection
        ("A", "F", True),  # Deep connection (A -> C -> E -> F)
        ("D", "F", True),  # Across graph (D -> B -> A -> C -> E -> F)
        ("A", "X", False), # Cannot reach disconnected island
        ("X", "F", False)  # Island cannot reach mainland
    ]
    
    all_passed = True
    print("--- Testing DFS Valid Path ---")
    for start, end, expected in test_cases:
        try:
            # We must pass None for visited so the set clears every new test!
            result = validPath(test_graph, start, end, visited=None)
            
            if result == expected:
                print(f"✅ PASS: Path from {start} to {end} -> {result}")
            else:
                print(f"❌ FAIL: {start} to {end} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: {start} to {end} threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
