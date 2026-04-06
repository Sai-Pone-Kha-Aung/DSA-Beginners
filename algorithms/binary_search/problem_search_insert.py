"""
PROBLEM: Search Insert Position (EASY)

Description:
Given a perfectly SORTED array of distinct integers and a `target` value, 
return the exact index if the `target` is strictly found. 

If it is NOT found, return the mathematical index where it absolutely WOULD be 
if it were inserted to keep the array perfectly sorted!

You must strictly write an algorithm with blazing fast O(log n) runtime complexity!

Example 1:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: 5 was successfully found exactly at index 2.

Example 2:
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: 2 is not in the array, but it belongs right between 1 and 3 (at index 1).

Example 3:
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: 7 is larger than everything in the array, so it sits at the very end (index 4).

Hint:
Use the standard Binary Search `while left <= right:` logic loop!
If you find the `target` perfectly, just return the `mid` index immediately.
If the while loop finishes entirely and you never found it... think about where 
your `left` and `right` pointers physically end up resting.
(Massive Spoiler Hint: When the loop breaks, the `left` pointer actually stops 
EXACTLY on the index where the new `target` item should gracefully be inserted!)
"""

def search_insert(nums, target):
    """
    Finds the target's exact index, or the index where it *should* be smoothly inserted.
    
    :param nums: list of int (completely SORTED)
    :param target: int
    :return: int
    """
    # 1. Establish your left and right outer boundaries
    # TODO: Initialize left and right pointers
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    # 2. Add your Binary Search "while" loop!
    # TODO: Implement the classic binary search logic here by calculating "mid"
    while left <= right:
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2


    # 3. If we escape the while loop without ever successfully returning `mid`, 
    # it means the target was never found anywhere.
    # Where does it mathematically belong now?
    # TODO: Return the correct final insertion index pointer
    return left


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),    # Target successfully exists
        ([1, 3, 5, 6], 2, 1),    # Target physically missing, goes in the middle
        ([1, 3, 5, 6], 7, 4),    # Target physically missing, goes at the extreme very end
        ([1, 3, 5, 6], 0, 0),    # Target physically missing, goes at the extreme beginning
        ([1], 0, 0)              # Single element array edge case
    ]
    
    all_passed = True
    print("--- Testing Search Insert Position ---")
    for nums, target, expected in test_cases:
        try:
            result = search_insert(nums, target)
            
            if result == expected:
                print(f"✅ PASS: nums={nums}, target={target} -> Index {result}")
            else:
                print(f"❌ FAIL: nums={nums}, target={target} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: nums={nums}, target={target} threw a Code Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
