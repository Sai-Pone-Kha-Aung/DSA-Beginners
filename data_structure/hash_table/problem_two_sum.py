"""
PROBLEM: Two Sum

Description:
Given an array of integers `nums` and an integer `target`, return the EXACT 
INDICES of the two numbers such that they add up to exactly the `target`.

You may assume that each input array would have EXACTLY ONE solution, and you 
may not use the exact same element index twice. You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return indices [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Because nums[1] + nums[2] == 6, we return indices [1, 2].

Hint (How to use a Hash Table for this):
A naive brute-force approach uses a double inner loop (O(n^2) time) to check every pair.
But we can do it in a single, lightning-fast pass (O(n) time) using a Hash Table 
(a standard Python Dictionary)!

As you loop through the array using `for index, num in enumerate(nums):`
1. Calculate the "complement" you need: `complement = target - num`
2. Check if that `complement` is already stored inside your Hash Table!
   - If it IS, boom! You found your pair. Return both of their indices.
   - If it ISN'T, simply save the current `num` into your Hash Table 
     (as the Key), and its `index` (as the Value), so the loop can find it later!
"""

def two_sum(nums, target):
    """
    Finds the indices of two numbers that add up to the target.
    
    :param nums: list of int
    :param target: int
    :return: list of int
    """
    # TODO: Initialize your Hash Table (dictionary) here
    result = {}
    
    # TODO: Loop through `nums`. 
    # Check if the complement is in the Hash Table.
    # If not, save the current number and its index!
    for i, num in enumerate(nums):
        x = target - num
        if x in result:
            return [result[x], i]

        result[num] = i

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]
    
    all_passed = True
    print("--- Testing Two Sum Hash Table ---")
    for nums, target, expected in test_cases:
        try:

            result = two_sum(nums, target)
            
            # Since [0, 1] and [1, 0] are technically both correct, we sort them for the test
            if result is not None and sorted(result) == sorted(expected):
                print(f"✅ PASS: nums={nums}, target={target} -> Returned {result}")
            else:
                print(f"❌ FAIL: nums={nums}, target={target} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: nums={nums}, target={target} threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
