"""
STRING DATA STRUCTURE

1. What is a String?
--------------------
A string is a linear data structure that represents a sequence of characters.
Under the hood, characters are stored as numerical values (like ASCII or Unicode) 
in memory. Strings are one of the most fundamental data structures in programming.

2. Immutability in Python:
--------------------------
In Python (and many other languages like Java), strings are IMMUTABLE. 
This means once a string is created, its contents cannot be changed in place.
Any operation that appears to modify a string (like replacement, splicing, or 
concatenation) actually creates an entirely new string object in memory!

3. Time Complexities in Python:
-------------------------------
- Access by index (e.g., s[2]): O(1)
- Search for character / substring: O(n) or O(n * m)
- Concatenation (s1 + s2): O(n + m) (since a new string is created)
- Slicing (s[i:j]): O(k) where k is the size of the slice
- Length (len(s)): O(1) (Python stores the length of strings explicitly)

4. Common Operations:
---------------------
Strings support many built-in operations for manipulation, parsing, 
and formatting, which makes them incredibly versatile.
"""

def demonstrate_string_basics():
    print("--- 1. String Basics & Immutability ---")
    my_string = "Hello"
    print(f"Original string: '{my_string}'")

    # Strings are indexed just like arrays:
    print(f"\nFirst character (my_string[0]): '{my_string[0]}'")
    print(f"\nLast character (my_string[-1]): '{my_string[-1]}'")

    # Trying to modify a string directly throws an error due to immutability:
    try:
        my_string[0] = "J"
    except TypeError as e:
        print(f"\nAttempting to change my_string[0] raised -> TypeError: {e}")
        
    # To "modify" a string, you must create a new one:
    new_string = "J" + my_string[1:]
    print(f"\nNew string after slicing and concatenation: '{new_string}'")


def demonstrate_string_operations():
    print("\n--- 2. Common String Operations ---")
    s = "  Data Structures and Algorithms  "
    print(f"\nOriginal string: '{s}'")
    
    # 1. Strip whitespace
    clean_s = s.strip()
    print(f"\nStripped string: '{clean_s}'")
    
    # 2. Split string into a list of substrings
    words = clean_s.split(" ")
    print(f"\nList of words (split): {words}")
    
    # 3. Join a list back into a string
    joined_s = "-".join(words)
    print(f"\nJoined string: '{joined_s}'")
    
    # 4. Search and Replace
    replaced_s = clean_s.replace("Algorithms", "Python")
    print(f"\nReplaced string: '{replaced_s}'")
    
    # 5. Iterating through a string
    print("\nIterating over the word 'Data':")
    for char in "Data":
        print(f" -> {char}")


if __name__ == "__main__":
    demonstrate_string_basics()
    demonstrate_string_operations()
