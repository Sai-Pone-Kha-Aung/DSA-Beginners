"""
DEPTH-FIRST SEARCH (DFS) - EASY EXPLANATION

1. What is DFS?
---------------
Breadth-First Search (BFS) explores "level by level" like ripples in a pond. 
Depth-First Search (DFS) explores "as far as possible down one path" before 
giving up and turning around.

Imagine you are in a massive physical Maze:
- BFS: You send 10 clones of yourself down every single possible hallway 
  simultaneously, map out 1 step, then 2 steps, then 3 steps.
- DFS: You (alone) pick one single hallway, run aggressively all the way to 
  the absolute end (a dead end), turn around, walk back to the last 
  intersection, and try the next hallway.

2. How does it work? (The Stack / Recursion)
--------------------------------------------
Because of how DFS explores down a single path, turns around, and remembers 
the last fork in the road, it intrinsically relies on a **STACK** (Last-In, First-Out).
  
Because Recursion intrinsically uses the Call Stack in memory, DFS is 
almost always written recursively! It makes the code incredibly short and elegant.

1. Mark the current node as VISITED.
2. Loop through all of its connecting neighbors.
3. If a neighbor hasn't been visited, instantly pause the loop and RECURSIVELY 
   dive into that neighbor! (Forcing the computer to go as deep as possible).
4. When it hits a dead end (no unvisited neighbors), the recursion naturally 
   unspools back to the previous intersection.

3. Time Complexity
------------------
O(V + E) -> Vertices + Edges.
Just like BFS, the worst-case scenario forces you to traverse every single 
node and every single connecting edge once.
"""

def dfs_recursive(graph, node, visited=None):
    """
    Performs a standard Depth-First Search on an Adjacency List recursively.
    """
    # 1. Initialize our beautifully simple Visited Set on the very first call
    if visited is None:
        visited = set()
        print("\n--- Starting DFS ---")

    # 2. The absolute first thing we do is conceptually "arrive" at the node!
    visited.add(node)
    print(f"Currently deep inside: {node}")

    # 3. Look at all the neighbors branching off this node
    for neighbor in graph[node]:
        
        # 4. If we haven't visited them, INSTANTLY dive all the way down that path!
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def demonstrate_dfs():
    # Let's create a Graph using an Adjacency List
    # 
    #       A --- B
    #       |     |
    #       C --- D --- E
    
    my_graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"]
    }
    
    # Run DFS starting at Node "A"
    print(f"Starting DFS recursively from 'A':")
    dfs_recursive(my_graph, "A")
    # Because A -> B -> D -> E -> (Dead End) -> C
    # Expected Output Order: A -> B -> D -> C -> E (or similar depending on dict order)

if __name__ == "__main__":
    demonstrate_dfs()
