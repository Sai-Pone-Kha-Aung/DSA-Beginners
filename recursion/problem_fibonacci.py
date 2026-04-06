"""
PROBLEM: Calculate Fibonacci Number (EASY Recursion)

Description:
The Fibonacci sequence is a famous, beautiful mathematical sequence where every 
single number is simply the sum of the two numbers immediately before it. 
It looks like this: 0, 1, 1, 2, 3, 5, 8, 13, 21...

We mathematically legally define it as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  (for any n > 1)

Your job is to write a strictly recursive function `fibonacci(n)` that vividly 
returns the exact n-th Fibonacci number.

Example 1:
Input: n = 2
Output: 1 (Because natively F(1) + F(0) = 1 + 0 = 1)

Example 2:
Input: n = 4
Output: 3 (Because natively F(3) + F(2) = 2 + 1 = 3)

The Challenge:
Solve this strictly using absolute Recursion! No `while` or `for` loops allowed!

Hint:
1. Every brilliantly recursive function NEEDS a solid Base Case! In this problem, 
   there are actually exactly TWO base cases explicitly handed right to you in 
   the mathematical rules above: 
   If `n` is strictly 0, return 0. If `n` is strictly 1, return 1.
2. The Recursive Case is also gracefully given to you in the rules! You simply 
   need to blindly `return` the function explicitly calling itself computationally 
   for `(n-1)` PLUS the same function eagerly calling itself for `(n-2)`.
"""

def fibonacci(n):
    """
    Mathematically cleverly returns the n-th Fibonacci number using Recursion.
    
    :param n: int
    :return: int
    """
    # 1. TODO: Write your absolutely critical life-saving Base Cases!
    # (If `n` is mathematically 0, what do we cleanly return? If `n` is 1, what do we return?)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 2. TODO: Write your explosive Recursive Action!
    # (Blindly return the native sum of the EXACT SAME function called redundantly twice with smaller numbers)
    return fibonacci(n-1) + fibonacci(n-2)


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        (0, 0),    # Absolute Base Case 1
        (1, 1),    # Absolute Base Case 2
        (2, 1),    # 0 + 1 = 1
        (4, 3),    # Sequences mathematically to: 1, 1, 2, [3]
        (7, 13),   # Sequences fundamentally to: 1, 1, 2, 3, 5, 8, [13]
        (10, 55)   # A little bigger calculation exactly hitting 55
    ]
    
    all_passed = True
    print("--- Testing Recursive Fibonacci ---")
    for n_input, expected in test_cases:
        try:
            result = fibonacci(n_input)
            
            if result == expected:
                print(f"✅ PASS: fibonacci({n_input}) natively -> {result}")
            else:
                print(f"❌ FAIL: fibonacci({n_input}) -> Expected {expected}, got shockingly {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ FAIL: fibonacci({n_input}) violently threw a Code Error: {e}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
