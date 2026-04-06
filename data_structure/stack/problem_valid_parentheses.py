"""
PROBLEM: Valid Parentheses

Description:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Hint:
A Stack (LIFO: Last-In, First-Out) is the perfect data structure for this! 
As you loop through the string:
- If you see an open bracket, PUSH it onto the stack.
- If you see a close bracket, POP from the stack and check if it matches the correct type.
(In Python, you can just use a normal list `[]` as a Stack using `.append()` and `.pop()`).

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([)]"
Output: False (The brackets are not closed in the correct inner-to-outer order!)

Example 5:
Input: s = "{[]}"
Output: True
"""

def is_valid_parentheses(s):
    """
    Checks if the parentheses in the string are valid.
    
    :param s: str
    :return: bool
    """
    # TODO: Implement your stack-based solution here!
    stack = []
    for i in s:
        #open
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        #close
        else:
            if not stack:
                return False
            
            top = stack.pop()

            if (i == ")" and top != "(") or \
                (i == "]" and top != "[") or \
                (i == "}" and top != "{"):
                return False
    
    return not stack
                

    


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[", False),
        ("]", False),
        ("", True)
    ]
    
    all_passed = True
    for s_input, expected in test_cases:
        result = is_valid_parentheses(s_input)
        if result == expected:
            print(f"✅ PASS: '{s_input}' -> {result}")
        else:
            print(f"❌ FAIL: '{s_input}' -> Expected {expected}, got {result}")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
