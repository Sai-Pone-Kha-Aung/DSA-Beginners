"""
PROBLEM: Insert the Last Element

Description:
You are given a perfectly sorted array, EXCEPT for the very last number, 
which is completely scrambled out of place! 

Your job is to cleanly "Insert" that mathematically messy last number into its 
exact correct position so the entire array magically becomes perfectly sorted.

Example 1:
Input: [2, 4, 6, 8, 3] 
(The '3' is completely out of place at the end! The rest of the array [2, 4, 6, 8] 
is perfectly sorted!)
Output: [2, 3, 4, 6, 8]

Example 2:
Input: [1, 2, 9, 4]
Output: [1, 2, 4, 9]

The Challenge:
This exact problem represents EXACTLY the inner loop of the incredibly formal 
Insertion Sort algorithm! By mastering this, you master the heart of the algorithm.
Do NOT use Python's built-in `.sort()` or `.insert()` shortcut functions!
You must manually pick up the last card, aggressively shift the BIGGER cards 
to the right to manually make an empty physical space, and expertly drop the 
card down into the exact safe slot!

Hint:
1. `current_card` = the very last element in the array (`arr[-1]`).
2. `compare_index` = starts at the second-to-last element (`len(arr) - 2`).
3. Keep shifting `arr[compare_index]` to the right as long as it is mathematically 
   BIGGER than your `current_card`!
4. When you successfully find a smaller card, drop `current_card` physically 
   into the brand new empty spot!
"""

def insert_last_element(arr):
    """
    Shifts a single out-of-place last element into a perfectly strictly sorted array.
    
    :param arr: list of int
    :return: list of int
    """
        
    # 1. Physically secretly pick up the very last card
    current = arr[-1]
    
    # 2. Start looking carefully at the card immediately to its left
    comp_index = len(arr) - 2
    
    # 3. Create your `while` loop!
    # TODO: While we haven't legally magically fallen off the left side of the array...
    while comp_index >= 0 and arr[comp_index] > current:
        arr[comp_index + 1] = arr[comp_index]
        comp_index -= 1
    
    arr[comp_index + 1] = current

    return arr




    # AND the `arr[compare_index]` card is strictly BIGGER than the `current_card`...
        # TODO: Aggressively shift the noticeably bigger card one spot to the right!
        # (e.g. arr[compare_index + 1] = arr[compare_index])
        # TODO: Move your eyes firmly one more card to the left (`compare_index -= 1`)
        
    # 4. We spectacularly found the empty spot! Safely drop the `current_card` permanently in.
    # TODO: Write the explicit physical drop logic!
    # (MASSIVE HINT: The empty spot is exactly safely sitting at `compare_index + 1`)
    
    # Return our gorgeously sorted array


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([2, 4, 6, 8, 3], [2, 3, 4, 6, 8]),
        ([1, 2, 9, 4], [1, 2, 4, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), # The last card magically was already perfect!
        ([9, 1], [1, 9]), # It has to painfully shift all the way to index 0
        ([10], [10]) # Edge case: A perfectly logically sorted hand of 1 single card
    ]
    
    all_passed = True
    print("--- Testing Single Card Insertion ---")
    for arr_input, expected in test_cases:
        # Make a perfect copy so we don't accidentally maliciously modify the test cases in-place
        original_arr = arr_input.copy()
        
        try:
            result = insert_last_element(original_arr)
            
            if result == expected:
                print(f"✅ PASS: Input {arr_input} -> Shifted manually to: {result}")
            else:
                print(f"❌ FAIL: Input {arr_input} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: Input {arr_input} threw a Code Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
