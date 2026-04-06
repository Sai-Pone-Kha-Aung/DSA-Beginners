"""
PROBLEM: Generate Binary Numbers using a Queue (EASY)

Description:
Given a number N, generate and return a list of the first N binary numbers 
using a strictly Queue data structure (First-In, First-Out).

You must build them manually using a Queue! 
Do not use Python's built-in `bin()` mathematical function!

Hint:
This is a classic Queue trick. 
1. Start by enqueuing the string "1" into your queue.
2. In a loop (doing this exactly N times):
   - Dequeue (pop from the FRONT) the element. Let's call it `front`.
   - Add `front` to your final answer list.
   - Take `front`, attach "0" to the end of it (e.g. `front + "0"`), and enqueue it!
   - Take `front`, attach "1" to the end of it (e.g. `front + "1"`), and enqueue it!

Example 1:
Input: N = 2
Output: ["1", "10"]

Example 2:
Input: N = 5
Output: ["1", "10", "11", "100", "101"]

"""

from collections import deque

def generate_binary_numbers(n):
    """
    Generates the first N binary numbers using a Queue.
    
    :param n: int
    :return: list of str
    """
    if n == 0:
        return []

    # TODO: Initialize your final answer `result` list here
    result = []

    # TODO: Initialize your Queue here (and put "1" inside it to start)
    queue = deque()
    queue.append("1")
    
    # TODO: Loop N times, popping the front, adding to results, and enqueuing new babies!
    for _ in range(n):
        first = queue.popleft()
        result.append(first)
        queue.append(first + "0")
        queue.append(first + "1")
    return result


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        (0, []),
        (2, ["1", "10"]),
        (5, ["1", "10", "11", "100", "101"]),
        (1, ["1"]),
        (10, ["1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010"])
    ]
    
    all_passed = True
    print("--- Testing Binary Generator ---")
    for n_input, expected in test_cases:
        try:
            result = generate_binary_numbers(n_input)
            if result == expected:
                print(f"✅ PASS: N={n_input} -> {result}")
            else:
                print(f"❌ FAIL: N={n_input} -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: N={n_input} threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
