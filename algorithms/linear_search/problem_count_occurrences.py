"""
PROBLEM: Count Occurrences

Description:
Given an unsorted array of integers `arr` and a `target` integer, return the 
total number of times the `target` appears in the array.

If the `target` does not exist in the array at all, return 0.

Example 1:
Input: arr = [1, 5, 3, 5, 2, 5], target = 5
Output: 3
Explanation: The number 5 appears exactly three times in the array.

Example 2:
Input: arr = [10, 20, 30], target = 99
Output: 0
Explanation: The number 99 is not in the array.

Example 3:
Input: arr = [7, 7, 7, 7], target = 7
Output: 4

Hint:
Linear Search is absolutely perfect for this! 
Usually, a standard Linear Search `return`s immediately and stops the moment 
it finds the target. But since we need to strictly count ALL occurrences, your 
`for` loop must never stop early! It must traverse the ENTIRE array from 
start to finish, mathematically adding `+1` to a running tally every time the 
`target` is spotted along the way!
"""

def count_occurrences(arr, target):
    """
    Counts how many times 'target' appears in 'arr' using Linear Search.
    
    :param arr: list of int
    :param target: int
    :return: int
    """
    # TODO: Create a counter variable starting at 0
    count = 0
    
    # TODO: Loop through every single element in `arr`.
    # If the current element matches your target, aggressively increase your counter!
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    
    # Return the final count
    return count
    


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 5, 2, 5], 5, 3),
        ([10, 20, 30], 99, 0),
        ([7, 7, 7, 7], 7, 4),
        ([], 5, 0),
        ([-1, 0, 1, -1], -1, 2)
    ]
    
    all_passed = True
    print("--- Testing Count Occurrences ---")
    for arr, target, expected in test_cases:
        try:
            result = count_occurrences(arr, target)
            
            if result == expected:
                print(f"✅ PASS: arr={arr}, target={target} -> Count is {result}")
            else:
                print(f"❌ FAIL: arr={arr}, target={target} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: arr={arr}, target={target} threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
