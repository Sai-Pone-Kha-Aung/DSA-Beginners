"""
PROBLEM: Find the Maximum Value in an Array

Description:
Given an array (list) of integers, write a function that finds and returns 
the maximum value in the array. You should not use the built-in max() function!

Example 1:
Input: [1, 5, 3, 9, 2]
Output: 9

Example 2:
Input: [-10, -3, -5, -1]
Output: -1

Example 3:
Input: [42]
Output: 42

"""

def find_maximum_value(arr):
    """
    Finds and returns the maximum value in the given array.
    
    :param arr: List[int]
    :return: int
    """
    # TODO: Implement your solution here!
    max_value = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

    # Hint: Start by assuming the first element is the maximum,
    # then iterate through the rest of the array to compare.
    pass


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 9, 2], 9),
        ([-10, -3, -5, -1, -2, -4], -1),
        ([42], 42),
        ([10, 10, 10, 10], 10),
        ([7, 4, 1, 8, 11, 2], 11)
    ]
    
    all_passed = True
    for arr, expected in test_cases:
        result = find_maximum_value(arr)
        if result == expected:
            print(f"✅ PASS: arr={arr} -> {result}")
        else:
            print(f"❌ FAIL: arr={arr} -> Expected {expected}, got {result}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
