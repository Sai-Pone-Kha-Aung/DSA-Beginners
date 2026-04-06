"""
GRAPH DATA STRUCTURE (EASY EXPLANATION)

1. What is a Graph?
-------------------
You just learned about Trees. A Tree is actually just a very specific, 
highly restricted type of Graph! (A tree is technically a "Directed Acyclic Graph", 
meaning the data only flows downwards, and there are absolutely 
no cyclical "loops" back to the top).

A Graph is essentially the Wild West of data structures. It is a completely free 
network of items where literally ANYTHING can connect to literally 
ANYTHING else. There is no strict "Root" node, and there is no maximum rule about 
how many connections a single node can have.

Think of social media platforms:
- You (a Node) are friends with Alice and Bob (Edges/Connections).
- Alice is friends with you and Charlie.
- Bob is friends with Charlie.
This creates a massive, looping web of connections. That's exactly what a Graph is!

2. Important Graph Terminology:
-------------------------------
- Vertex (Plural: Vertices): The actual data points stored in the structure 
  (like a user on Facebook, or a city mapped on Google Maps). 
  This is the exact same thing as a "Node" in a Tree.
- Edge: The connection or link between two Vertices 
  (like a friendship tying two users together, or a physical highway).
- Directed Graph: The connections flow only ONE WAY. (e.g., Twitter/X: 
  You can follow a celebrity, but they don't automatically follow you back).
- Undirected Graph: The connections go BOTH WAYS 
  automatically. (e.g., Facebook: If you are friends with someone explicitly, 
  they are forced to be friends with you).
- Weighted Graph: The specific edges have a "cost" attached to them. 
  (e.g., Google Maps: the highway connecting City A to City B takes exactly 45 minutes).

3. How do we store a Graph in Code? (Adjacency List)
----------------------------------------------------
Unlike a Tree where we build physical `Node` objects that point to `left` and 
`right`, the absolute easiest way to store a Graph is by simply using a Hash Table 
(a standard Python Dictionary)!

We map each Vertex (Key) to a List of all the Vertices it connects to (Value).

For example:
friendships = {
    "You": ["Alice", "Bob"],
    "Alice": ["You", "Charlie"],
    "Bob": ["Charlie"],
    "Charlie": ["Alice", "Bob"]
}

4. Time Complexities:
---------------------
- Using an Adjacency List (Dictionary), adding a new Vertex or Edge is blazing 
  fast: O(1) time!
- To properly search through a Graph, we use famous search algorithms like 
  Breadth-First Search (BFS) or Depth-First Search (DFS), which conceptually 
  take O(V + E) time (Vertices + Edges).
"""

# ==========================================
# --- Basic Graph Implementation ---
# ==========================================

class Graph:
    """A simple Undirected Graph using an Adjacency List."""
    
    def __init__(self):
        # We will store our graph as a standard Python Dictionary
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Adds a new node/user to our graph."""
        # If the user doesn't exist yet, give them an empty friends list!
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Builds an Undirected (two-way) connection between two vertices."""
        # 1. Make sure both vertices exist!
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
            
        # 2. Because this is an Undirected Graph (like Facebook friendships)...
        # We add each vertically to the other's friend list!
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        """Prints out the entire graph!"""
        print("--- Your Graph (Social Network) ---")
        for vertex in self.adjacency_list:
            connections = ", ".join(self.adjacency_list[vertex])
            print(f"{vertex} is connected to: [{connections}]")


def demonstrate_graph():
    # 1. Initialize our empty graph
    social_network = Graph()
    
    # 2. Add some users (Vertices) 
    social_network.add_vertex("Alice")
    social_network.add_vertex("Bob")
    social_network.add_vertex("Charlie")
    social_network.add_vertex("David")
    
    # 3. Create some friendships (Edges)
    social_network.add_edge("Alice", "Bob")
    social_network.add_edge("Alice", "Charlie")
    social_network.add_edge("Bob", "David")
    social_network.add_edge("Charlie", "David")
    
    # Notice: We never explicitly told Alice to connect to David!
    
    # 4. Print our mapped graph!
    social_network.display()

if __name__ == "__main__":
    demonstrate_graph()
