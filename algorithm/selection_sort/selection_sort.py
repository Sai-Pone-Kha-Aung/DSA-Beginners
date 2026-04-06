"""
SELECTION SORT (EASY EXPLANATION)

1. What is Selection Sort?
--------------------------
Imagine you have a messy deck of cards in your hand, and you desperately want 
to sort them from smallest to largest. 

How do you do it?
You scan through the entire pile of cards, looking for the absolute 
SMALLEST card (the Ace!). Once you finally find it, you pull it out and stick  
it at the very front of the deck. 

Now, the first spot in your deck is perfectly sorted!
Then, you scan through all the *remaining* messy cards, looking for the 
*next* smallest card (the 2!). You pull it out, and stick it right behind the Ace. 
You repeat this exact process of "selecting" the smallest remaining card and 
moving it to the front until your whole deck is perfectly organized.

This is exactly what Selection Sort does natively in code!

2. How does the code work?
--------------------------
It requires a standard "Nested Loop" (a loop inside a loop).
- The OUTER loop acts as an invisible boundary. It marks where the "sorted" section 
  of our deck currently ends. (It slowly moves right: index 0, index 1, index 2...)
- The INNER loop systematically walks through the unsorted messy right side of 
  the deck, aggressively hunting for the absolute smallest number.
- Once the inner loop firmly finds the smallest number, it Swaps it 
  with whatever card is currently sitting at the outer loop's boundary!

3. Time Complexities:
---------------------
- Best Case: O(n^2) -> Even if the array is perfectly sorted, Selection Sort 
  is totally legally "blind". It mathematically HAS to forcefully scan through all 
  the remaining cards every single time just to make sure there isn't a smaller 
  one hiding at the very end. (Unlike Bubble Sort, it can never quit early!)
- Worst/Average Case: O(n^2) -> The array is backwards or scrambled. You 
  painstakingly scan through all `n` items to find the smallest, then aggressively 
  scan `n-1` items to find the next smallest, etc...

4. When to use it?
------------------
Like Bubble Sort, it is mostly an educational tool and dreadfully slow for big databases. 
However, it does have one tiny structural advantage over Bubble Sort: it makes 
significantly fewer physical "swaps" (only exactly 1 swap per outer loop, whereas 
Bubble Sort physically swaps constantly). If "writing to memory" is incredibly 
expensive/dangerous on a specific piece of hardware, Selection Sort is slightly 
safer than Bubble Sort!
"""

def selection_sort(arr):
    """
    Sorts an array using the manual Selection Sort algorithm.
    
    :param arr: A List of unsorted items
    :return: The perfectly sorted List
    """
    n = len(arr)
    
    # 1. Outer loop: Creates an ever-moving invisible boundary between 
    # the "Sorted Left" side and the "Messy Right" side of the array.
    for i in range(n):
        
        # Let's naively assume the VERY FIRST card in the messy section is the smallest...
        min_index = i
        
        # 2. Inner loop: Scan through all the remaining messy cards 
        # specifically hunting for anything even smaller!
        for j in range(i + 1, n):
            
            # Did we find a new, shockingly smaller card?
            if arr[j] < arr[min_index]:
                
                # Update our brain's memory! Mark down this new winner's exact index location.
                min_index = j
                
        # 3. We finished scanning! We found the absolute smallest messy card!
        # Now, physically Swap that card straight to the safety of our front 
        # "Sorted boundary" (index i)
        arr[i], arr[min_index] = arr[min_index], arr[i]
            
    # Return our gorgeously sorted array
    return arr


def demonstrate_selection_sort():
    print("--- Selection Sort Demonstration ---")
    
    my_unordered_list = [64, 25, 12, 22, 11]
    print(f"Original scrambled list: {my_unordered_list}\n")
    
    # Run our sorting algorithm!
    sorted_list = selection_sort(my_unordered_list.copy())
    
    print(f"✅ Perfectly sorted list:  {sorted_list}")


if __name__ == "__main__":
    demonstrate_selection_sort()
