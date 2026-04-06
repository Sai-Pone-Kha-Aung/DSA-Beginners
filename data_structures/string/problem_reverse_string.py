"""
PROBLEM: Reverse a String

Description:
Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".

Important Constraints:
- Do NOT use Python's built-in string slicing trick (like `s[::-1]`).
- Do NOT use the built-in `reversed()` function.
- Try to iterate through the string and build the reversed string manually!

Example 1:
Input: "hello"
Output: "olleh"

Example 2:
Input: "Data Structures"
Output: "serutcurtS ataD"

Example 3:
Input: "racecar"
Output: "racecar"

"""

def reverse_string(s):
    """
    Reverses the given string.
    
    :param s: str
    :return: str
    """
    # TODO: Implement your solution here!
    rev_string = ""

    for i in range(len(s)):
        rev_string = s[i] + rev_string

    return rev_string


# ==========================================
# --- Tests: Do not modify below this line ---
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("Data Structures", "serutcurtS ataD"),
        ("racecar", "racecar"),
        ("a", "a"),
        ("", ""),
        ("12345", "54321")
    ]
    
    all_passed = True
    for s_input, expected in test_cases:
        result = reverse_string(s_input)
        if result == expected:
            print(f"✅ PASS: '{s_input}' -> '{result}'")
        else:
            print(f"❌ FAIL: '{s_input}' -> Expected '{expected}', got '{result}'")
            all_passed = False
            
    if all_passed:
        print("\n🎉 Awesome! All tests passed!")
    else:
        print("\nKeep trying! Some tests failed.")
