"""
BUBBLE SORT (EASY EXPLANATION)

1. What is Bubble Sort?
-----------------------
Imagine you have a line of varying height kindergarteners, and you need to 
sort them from shortest to tallest. 

How do you do it?
You look at the VERY FIRST pair of kids. If the kid on the left is TALLER than 
the kid on the right, you make them physically swap places. 
Then, you move one kid down the line and compare the NEXT pair. You keep swapping 
any adjacent pair that is standing in the wrong order.

By the time you finish walking down the entire line, the absolute TALLEST kid 
will have successfully swapped his way all the way to the very end of the line! 
(Like a heavy object sinking to the bottom, or a "bubble" floating to the top).

But the rest of the line might still be mixed up! So you walk back to the 
front and do it all over again. You keep repeating this entire process until 
you walk through the whole line without needing to swap anyone.

2. How does the code work?
--------------------------
It requires a "Nested Loop" (a loop inside a loop).
- The OUTER loop keeps the entire process repeating over and over again.
- The INNER loop walks through the array, comparing `arr[j]` with right next 
  to it `arr[j+1]` and actively swapping them if they are backwards.

3. Time Complexities:
---------------------
- Best Case: O(n) -> The array is miraculously ALREADY perfectly sorted. You 
  walk through the line once, make zero swaps, and instantly realize your 
  work is done!
- Worst/Average Case: O(n^2) -> The array is completely backwards 
  (e.g., `[9, 8, 7, 1]`). You have to painstakingly swap every single element 
  down the entire line, over and over again. Because it uses nested loops, 
  it gets exponentially slower the more items you have.

4. When to use it?
------------------
Almost NEVER in the real world! Bubble sort is famous simply because it is the 
absolute easiest sorting algorithm to conceptually understand and write from scratch. 
But it is practically unusable for massive databases. It is considered an 
"educational" baseline algorithm. (Languages use far faster algorithms like 
Merge Sort or Timsort behind the scenes).
"""

def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    :param arr: A List of unsorted items
    :return: The perfectly sorted List
    """
    n = len(arr)
    
    # 1. Outer loop: tells us how many times we need to run the inner swapping process
    for i in range(n):
        
        # A smart tracker flag! Let's assume the list is already flawless this time
        already_sorted_perfectly = True
        
        # 2. Inner loop: Walks down the line comparing adjacent pairs.
        # Notice we only go up to `(n - 1 - i)` because the last `i` elements 
        # have already firmly "bubbled" to their correct final spots! 
        # Nobody needs to re-check the tallest kids at the end.
        for j in range(0, n - i - 1):
            
            # 3. Are these two kids standing in the wrong order?
            if arr[j] > arr[j + 1]:
                
                # SWAP THEM! (Python makes swapping beautifully simple)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # We definitively had to swap someone, so it wasn't flawless yet!
                already_sorted_perfectly = False
                
        # 4. If we walked through the entire line and nobody swapped at all...
        # It means the line is completely sorted! We can beautifully quit early!
        if already_sorted_perfectly:
            break
            
    return arr


def demonstrate_bubble_sort():
    print("--- Bubble Sort Demonstration ---")
    
    my_unordered_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original scrambled list: {my_unordered_list}\n")
    
    # Run our sorting algorithm!
    sorted_list = bubble_sort(my_unordered_list.copy())
    
    print(f"✅ Perfectly sorted list:  {sorted_list}")


if __name__ == "__main__":
    demonstrate_bubble_sort()
