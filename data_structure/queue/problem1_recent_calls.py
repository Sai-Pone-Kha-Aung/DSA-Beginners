"""
PROBLEM: Number of Recent Calls

Description:
You are building a system that tracks how many incoming network requests 
(or "pings") happen within a specific time window. 
You need to implement the `RecentCounter` class.

Requirements:
- `__init__()` Initializes the counter with zero recent requests.
- `ping(t)` Adds a new request at time `t` (in milliseconds), and returns the 
  total number of requests that have happened in the past exactly 3000 milliseconds.
  (inclusive range: [t - 3000, t]).

Important Constraint:
You are guaranteed that every call to `ping` uses a strictly larger value of `t` 
than the previous call. It always moves forward in time.

Hint:
A Queue (FIFO: First-In, First-Out) is absolutely perfect for a "sliding window" of time. 
Since time `t` is always increasing, you can just append the new time `t` to the right 
side of your queue, and then keep removing (popping) from the LEFT side of the queue 
until the oldest timestamp at the front is finally within the valid [t - 3000, t] window!

(In Python, you can use `collections.deque` to create a Queue that has lightning FAST 
O(1) pops from the left side using `my_queue.popleft()`).
"""

import collections

class RecentCounter:
    def __init__(self):
        # TODO: Initialize your Queue here!
        pass

    def ping(self, t):
        """
        Adds the request at time t and returns the number of valid 
        requests in the past 3000ms.
        
        :param t: int (timestamp in milliseconds)
        :return: int
        """
        # TODO: Implement your logic here!
        pass


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    counter = RecentCounter()
    
    # Each tuple is (time_t, expected_return_value)
    test_calls = [
        (1, 1),       # range [-2999, 1] includes [1]. Returns 1
        (100, 2),     # range [-2900, 100] includes [1, 100]. Returns 2
        (3001, 3),    # range [1, 3001] includes [1, 100, 3001]. Returns 3
        (3002, 3),    # range [2, 3002] includes [100, 3001, 3002]. Returns 3 ('1' is too old and gets popped!)
        (7000, 1),    # range [4000, 7000] includes [7000]. Returns 1 (all previous requests are popped!)
    ]
    
    all_passed = True
    print("--- Testing RecentCounter Sliding Window ---")
    for t_input, expected in test_calls:
        # We wrap in a try-except just in case ping() isn't returning an int yet
        try:
            result = counter.ping(t_input)
            if result == expected:
                print(f"✅ PASS: ping({t_input}) -> {result} recent calls")
            else:
                print(f"❌ FAIL: ping({t_input}) -> Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: ping({t_input}) threw an Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
