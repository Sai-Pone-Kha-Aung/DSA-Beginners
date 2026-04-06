"""
PROBLEM: Find the K-th Smallest Element (EASY)

Description:
Given an array of completely unsorted numbers and an integer `k`, magically 
find the `k`-th smallest element in the array.

Example 1:
Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: The 3rd smallest element is 7. (The true sorted order is 3, 4, 7...)

Example 2:
Input: arr = [7, 10, 4, 3, 20, 15], k = 4
Output: 10
Explanation: The 4th smallest element is 10. (The true sorted order is 3, 4, 7, 10...)

The Challenge:
Solve this by writing a smartly modified Selection Sort algorithm!
You are NOT allowed to simply use Python's fast `.sort()` and return `arr[k-1]`!

Massive Hint (Why this problem is absolutely perfect for Selection Sort):
Look very closely at how Selection Sort natively works. 
- In the very first outer loop pass, it miraculously finds the absolute 1st smallest 
  item in the array and perfectly locks it into index 0.
- In the second outer loop pass, it forcefully finds the exactly 2nd smallest item 
  and perfectly locks it into index 1.
- In the third outer loop pass, it aggressively finds the exactly 3rd smallest item!

Wait! Do you actually need to perfectly sort the *entire* array of 1,000,000 items 
if I just vaguely ask you to quickly hand me the 3rd smallest item? No! 
You legally only need to run the Selection Sort outer loop exactly `k` times, 
instantly break/stop, and blindly return the newest item you just locked into place!
"""

def find_kth_smallest(arr, k):
    """
    Finds the strictly k-th smallest element using a partial Selection Sort.
    
    :param arr: list of int
    :param k: int
    :return: int
    """
    n = len(arr)
    
    # TODO: Write your Selection Sort outer for-loop!
    for i in range(n):
        min_index = i
        # TODO: Write your inner loop to find the blinding minimum!
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # TODO: Physically excitedly Swap the new minimum value to the front 
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # 'sorted' invisible boundary
        
    # TODO: Return the exact k-th smallest element! 
    # (Where exactly is it naturally physically sitting securely right now?)
    return arr[k-1]


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 3, 20, 15], 4, 10),
        ([1, 2, 3, 4, 5], 1, 1), # Best case: asking for the 1st
        ([5, 4, 3, 2, 1], 5, 5), # Worst case: asking for the absolute last
        ([100], 1, 100) # Edge case: single item
    ]
    
    all_passed = True
    print("--- Testing Selection Sort (K-th Smallest) ---")
    for arr_input, k, expected in test_cases:
        # Make a perfect copy so we don't accidentally maliciously modify the test cases in-place
        original_arr = arr_input.copy()
        
        try:
            result = find_kth_smallest(original_arr, k)
            
            if result == expected:
                print(f"✅ PASS: Input {arr_input}, k={k} -> Found: {result}")
            else:
                print(f"❌ FAIL: Input {arr_input}, k={k} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: Input {arr_input}, k={k} threw a Code Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
