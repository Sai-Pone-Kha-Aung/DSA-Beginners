"""
PROBLEM: Sort Strings by Length (EASY Bubble Sort)

Description:
You are given an array of strings. You need to manually sort the array so that 
the SHORTEST strings safely bubble to the front, and the LONGEST strings bubble 
all the way to the back.
If two strings have the exact same length, their physical order doesn't matter.

Example 1:
Input: ["apple", "pie", "banana", "kiwi"]
Output: ["pie", "kiwi", "apple", "banana"]

Example 2:
Input: ["a", "abc", "ab"]
Output: ["a", "ab", "abc"]

The Challenge:
Solve this strictly by writing a custom Bubble Sort algorithm from scratch!
You are NOT allowed to use Python's fast built-in `.sort()` or `sorted()` functions!

Hint:
Use the standard Bubble Sort nested-loop format we just learned:
- The outer loop faithfully runs `n` times.
- The inner loop walks down the array thoroughly checking adjacent pairs.
- BUT instead of comparing the words directly (e.g. `arr[j] > arr[j+1]`), 
  you need to mathematically compare their LENGTHS! 
  (e.g., `let left_length = len(arr[j])`)
"""

def sort_by_length(arr):
    """
    Sorts an array of strings strictly by their length using Bubble Sort.
    
    :param arr: list of str
    :return: list of str
    """
    n = len(arr)
    # TODO: Write your outer for-loop!
    for i in range(n):
        # TODO: Write your inner for-loop!
        for j in range(i+1, n):
            # TODO: If the word on the left is 'longer' than the word on the right...
            if len(arr[i]) > len(arr[j]):
            # Swap them physically!
                arr[i], arr[j] = arr[j], arr[i]
            
    # Don't forget to return the modified array
    return arr


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        (["apple", "pie", "banana", "kiwi"], ["pie", "kiwi", "apple", "banana"]),
        (["a", "abc", "ab"], ["a", "ab", "abc"]),
        (["hello", "world"], ["hello", "world"]), # Exact same length
        (["longest", "short", "tiny", "a"], ["a", "tiny", "short", "longest"]),
        ([], []) # Empty array edge-case
    ]
    
    all_passed = True
    print("--- Testing Bubble Sort (By String Length) ---")
    for arr_input, expected in test_cases:
        # We smartly make a copy so we don't accidentally modify the test cases in-place
        original_arr = arr_input.copy()
        try:
            result = sort_by_length(original_arr)
            
            # To test completely accurately, we map both output arrays to their lengths.
            # (Because words of the exact same length can be swapped and still perfectly 'correct')
            result_lengths = [len(word) for word in result] if result is not None else []
            expected_lengths = [len(word) for word in expected] if expected else []
            
            if result is not None and result_lengths == expected_lengths:
                print(f"✅ PASS: Input {arr_input} -> Sorted sizes: {result}")
            else:
                print(f"❌ FAIL: Input {arr_input} -> Expected lengths {expected_lengths}, got {result_lengths} ({result})")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: Input {arr_input} threw a Code Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
