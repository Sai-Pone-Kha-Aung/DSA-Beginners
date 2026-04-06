"""
BREADTH-FIRST SEARCH (BFS) - EASY EXPLANATION

1. What is BFS?
---------------
Breadth-First Search (BFS) is a classic algorithm for exploring
a Graph or a Tree.

The key rule of BFS: Explore in RIPPLES! (Level by Level).
Imagine dropping a stone in a pond. The ripples hit everything
1 inch away, then 2 inches away, then 3 inches away.

If you start looking for a friend on Facebook using BFS:
- First, you check ALL of your direct friends (Level 1).
- Then, you check ALL of their friends (Level 2).
- Then, ALL of their friends (Level 3).

2. How does it work? (The Queue)
--------------------------------
To force the computer to search level-by-level, BFS famously uses
a **QUEUE** (First-In, First-Out).

1. Put the starting node in the Queue.
2. While the Queue is not empty:
   - Pop the first person in line out of the Queue.
   - If they are the target, you win!
   - If not, add ALL of their unvisited connections to the BACK of the Queue.
3. Because new connections go to the BACK, you are guaranteed to finish
   checking everyone in Level 1 before you ever touch Level 2!

3. Time Complexity
------------------
O(V + E) -> Vertices + Edges.
In the worst case, you literally have to check every single node (V)
and every single connecting line (E) in the entire graph.
"""

from collections import deque

def bfs(graph, start_node):
    """
    Performs a standard Breadth-First Search on an Adjacency List.
    """
    # 1. We need a Queue to keep track of who to visit next
    # We initialize it with our very first node.
    queue = deque([start_node])
    
    # 2. We need a Set to keep track of who we've already visited!
    # (Otherwise, in a Graph with loops, we would search in circles forever!)
    visited_nodes = set([start_node])
    
    print("\n--- Starting BFS ---")
    
    # 3. Process the Queue until it is completely empty
    while queue:
        # 4. Take the next person out of the front of the line
        current = queue.popleft()
        print(f"Just visited: {current}")
        
        # 5. Look at all of their direct connections
        for neighbor in graph[current]:
            # 6. If we haven't visited them yet, add them to the queue AND the visited list!
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor) # Add to the BACK of the line!


def demonstrate_bfs():
    # Let's create a Graph using a simple Python Dictionary (Adjacency List)
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
    
    # Run BFS starting at Node "A"
    print(f"Starting BFS from 'A':")
    bfs(my_graph, "A")
    # Expected Output Order: A -> B -> C -> D -> E
    
    # Run BFS starting at Node "E"
    print(f"\nStarting BFS from 'E':")
    bfs(my_graph, "E")
    # Expected Output Order: E -> D -> B -> C -> A

if __name__ == "__main__":
    demonstrate_bfs()
