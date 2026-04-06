"""
INSERTION SORT (EASY EXPLANATION)

1. What is Insertion Sort?
--------------------------
Imagine you are playing a card game and the dealer hands you cards one-by-one.
When you receive your very first card, your hand is technically "sorted".
When you receive your second card, you look at it and smoothly slide it 
either BEFORE or AFTER your first card. 
When you receive your third card, you scan the cards already in your hand 
from right-to-left, find the exact correct spot, and slide it in!

This is exactly how Insertion Sort mechanically works!
It sequentially builds a perfectly "sorted" deck on the left side of the array 
one card at a time. It takes a messy card from the right side, and physically 
shifts the already-sorted cards over so it can "insert" the messy card precisely 
where it belongs.

2. How does the code work?
--------------------------
We use a loop to logically walk through every single item starting at `index 1`.
(Because an array of just 1 item sitting at `index 0` is already sorted flawlessly!)

For every new "card" we inspect:
- We save its value (we physically pick the card up out of the array).
- We look at all the sorted cards to our left.
- If those sorted cards are BIGGER than our card, we aggressively shift them 
  one spot to the right to make an empty room.
- Once we successfully find a smaller card (or hit the very start of the list), 
  we elegantly drop our card straight into the newly opened empty slot!

3. Time Complexities:
---------------------
- Best Case: O(n) -> The amazing thing about Insertion Sort is that if the 
  list is ALREADY perfectly sorted or ALMOST sorted, it checks the card to 
  its left, goes "Oh, I'm already bigger than you," and instantly moves on. 
  It runs blisteringly fast on mostly-sorted real-world data!
- Worst/Average Case: O(n^2) -> The array is brutally completely backwards 
  (e.g., `[9, 8, 7, 1]`). Every single time you pick up a card, you have to 
  painfully shift every single other card in your hand to the right to cram 
  it into the front.

4. When to use it?
------------------
Insertion Sort is shockingly practical in the professional world! 
If your data is "almost sorted" (e.g., streaming live data where most 
things arrive in chronological order), Insertion Sort absolutely dominates.
In fact, Python's incredibly famous and lightning-fast built-in `.sort()` 
algorithm (called Timsort) is genuinely a super-hybrid that actually uses 
Insertion Sort under the hood for small chunks of numbers!
"""

def insertion_sort(arr):
    """
    Sorts an array natively using the Insertion Sort algorithm.
    
    :param arr: A list of unsorted items
    :return: The perfectly sorted list
    """
    
    # 1. We purposefully start at index 1 because the very first item (index 0) 
    # is mechanically considered a "flawlessly sorted hand of 1 card".
    for i in range(1, len(arr)):
        
        # 2. Pick up the newest messy card in our hand
        current_card = arr[i]
        
        # 3. We will start comparing it to the card immediately sitting to its left
        compare_index = i - 1
        
        # 4. While we haven't magically fallen off the front of the array...
        # AND while the sorted cards to our left are actually BIGGER than our current card...
        while compare_index >= 0 and arr[compare_index] > current_card:
            
            # Shift the bigger card one physical spot to the right to make an empty space!
            arr[compare_index + 1] = arr[compare_index]
            
            # Move our eyes one more card to the left to eagerly check the next one
            compare_index -= 1
            
        # 5. We finally found a smaller card (or hit the brick wall)! 
        # Safely drop our current card permanently into the exact empty slot we just created.
        arr[compare_index + 1] = current_card
        
    # Return our gorgeously sorted array
    return arr


def demonstrate_insertion_sort():
    print("--- Insertion Sort Demonstration ---")
    
    my_unordered_list = [12, 11, 13, 5, 6]
    print(f"Original scrambled list: {my_unordered_list}\n")
    
    # Run our sorting algorithm!
    sorted_list = insertion_sort(my_unordered_list.copy())
    
    print(f"✅ Perfectly sorted list:  {sorted_list}")


if __name__ == "__main__":
    demonstrate_insertion_sort()
