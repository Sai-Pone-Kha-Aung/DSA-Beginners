"""
PROBLEM: Shortest Path in a Maze

Description:
You are given a 2D grid representing a maze.
- `0` represents an empty space (you can walk here).
- `1` represents a wall (you CANNOT walk here).

You start at `start` coordinate (row, col) and want to reach `target` coordinate.
Find the EXACT minimum number of steps to reach the target.
If it is impossible to reach the target, return -1.

You can move Up, Down, Left, or Right.

Example:
maze = [
  [0, 0, 0, 0],
  [1, 1, 0, 1],
  [0, 0, 0, 0],
  [0, 1, 1, 0]
]
start = (0, 0)
target = (3, 3)

The shortest path is 6 steps.

Hint:
This is heavily based on the exact BFS template you just learned!
Here, your "graph" is the 2D grid itself. 
The "neighbors" of a cell (r, c) are the valid adjacent cells that are not walls (0).

Instead of just putting `current_cell` into the Queue, try safely putting a Tuple inside 
the Queue! Example: `queue.append(((r, c), current_distance))`
"""

from collections import deque

def shortest_path_in_maze(maze, start, target):
    """
    Finds the minimum number of steps to reach the target in a maze.
    """
    ROWS = len(maze)
    COLS = len(maze[0])
    
    # Check if start or target is a wall
    if maze[start[0]][start[1]] == 1 or maze[target[0]][target[1]] == 1:
        return -1
        
    # 1. TODO: Initialize the Queue with a tuple containing (start_coordinate, distance)
    # Example: queue = deque([(start, 0)])
    queue = deque([(start, 0)]) 
    
    # 2. TODO: Initialize your visited set to avoid loops. Add the 'start' coordinate.
    visited = {start} 
    
    # 3. Process the Queue!
    while queue:
        # TODO: Pop the front of the queue
        current_cell, current_distance = queue.popleft()
        
        # TODO: Check if we reached the target!
        # If so, return current_distance
        if current_cell == target:
            return current_distance
        
        # TODO: Get neighbors (up, down, left, right)
        # Directions you can move: up (-1, 0), down (1, 0), left (0, -1), right (0, 1)
        # For each valid neighbor (inside grid, not a wall, not visited):
        #   - Add them to the visited set
        #   - Add them to the Queue with (distance + 1)

        r, c = current_cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] == 0:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_distance + 1))
    return -1


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================

maze_1 = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

maze_2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

if __name__ == "__main__":
    test_cases = [
        (maze_1, (0, 0), (3, 3), 6),  
        (maze_1, (0, 0), (0, 3), 3),    
        (maze_2, (0, 0), (0, 2), 6),  
        (maze_2, (0, 0), (2, 2), 4),    
        (maze_2, (0, 0), (1, 1), -1) # unreachable (wall)
    ]
    
    all_passed = True
    print("--- Testing BFS Shortest Path in Maze ---")
    for i, (m, start, target, expected) in enumerate(test_cases, 1):
        try:
            result = shortest_path_in_maze(m, start, target)
            
            if result == expected:
                print(f"✅ PASS Test {i}: Start {start} to Target {target} is {result} steps")
            else:
                print(f"❌ FAIL Test {i}: {start} to {target} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL Test {i}: Threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
