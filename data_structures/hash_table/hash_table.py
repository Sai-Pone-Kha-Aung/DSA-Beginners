"""
HASH TABLE DATA STRUCTURE (EASY EXPLANATION)

1. What is a Hash Table?
------------------------
Imagine you are at a massive library with millions of books. If you want to 
find a specific book, you wouldn't start at Shelf #1 and check every single 
book one by one (that would take forever, or O(n) time).

Instead, you use a library catalog. You look up the book's title, and the 
catalog INSTANTLY tells you the EXACT shelf and row where the book is located. 
You walk straight there and grab it (which takes O(1) time).

A Hash Table is exactly that: a computer's "Instant Catalog". 
To use one, you always store "Key-Value pairs". Instead of searching through 
an entire list to find your Value, a Hash Table takes your Key and uses a 
clever math trick to instantly jump to the exact location of the Value!

2. How does the "Math Trick" work?
----------------------------------
The trick is a mathematical formula called a Hash Function.

Let's say you want to store a person's phone number.
- Key: "Alice"
- Value: "555-1234"

1. The Hash Function takes the Key ("Alice"), mathematically scrambles the 
   letters, and turns it into a simple number (e.g., Alice -> translates to -> index 4).
2. The computer safely stores the Value ("555-1234") at array index 4.

Later, when you want to look up Alice's phone number, the Hash Function 
looks at "Alice", immediately calculates the number 4 again, and instantly 
grabs the phone number from index 4! No searching required.

3. Hash Tables in Python:
-------------------------
You likely already use them! In Python, Hash Tables are built directly into the 
language as "Dictionaries" (the `{key: value}` syntax). Under the hood, Python 
runs the Hash Function for you automatically.

4. Time Complexities:
---------------------
Because the Hash Function jumps instantly to the correct memory index:
- Insert: O(1)
- Delete: O(1)
- Lookup/Search: O(1)

(Note: Very rarely, two different keys might mathematically accidentally translate 
to the exact same number, which is called a "Collision". In the absolute worst-case 
scenario where everything collides, it could take O(n) time, but modern Hash 
Functions prevent this flawlessly!)
"""


def demonstrate_hash_table():
    print("--- Python's Built-in Hash Table (Dictionary) ---")
    
    # 1. Creating a hash table
    # "Key" on the left, "Value" on the right
    phone_book = {
        "Alice": "555-1234",
        "Bob": "555-9876",
        "Charlie": "555-0000"
    }
    
    # 2. Lookup data instantly (O(1) time!)
    # The computer hashes "Alice" and instantly finds her number
    print(f"Look up Alice's number instantly: {phone_book['Alice']}")
    
    # 3. Add new data instantly (O(1) time!)
    phone_book["Diana"] = "555-1111"
    print(f"Added Diana! Her number is: {phone_book['Diana']}")
    
    # 4. Check if a Key exists instantly (O(1) time!)
    # This does not scan the whole dictionary, it hashes "Bob" and jumps!
    if "Bob" in phone_book:
        print("Bob exists in the catalog!")
        
    # 5. Delete data instantly (O(1) time!)
    del phone_book["Charlie"]
    print(f"Deleted Charlie. Current Phone Book: {phone_book}")


if __name__ == "__main__":
    demonstrate_hash_table()
