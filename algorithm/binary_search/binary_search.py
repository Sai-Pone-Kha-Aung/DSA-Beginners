"""
BINARY SEARCH (EASY EXPLANATION)

1. What is Binary Search?
-------------------------
Imagine you are looking for the word "Zebra" in a heavy 1,000-page dictionary.
Linear Search would have you open page 1, check every word, go to page 2, 
check every word... mechanically reading 1,000 pages until you find it. (O(n) time).

But you wouldn't actually do that! 
Because the dictionary is perfectly SORTED alphabetically, you intuitively 
open it right down the MIDDLE.
You land on the letter "M". Since you know "Z" comes AFTER "M", you instantly 
realize that "Zebra" is absolutely not in the left half of the book. 
You can instantly ignore 500 pages, throw away the left side, and only look at 
the right side! You then find the middle of the right side... and keep slicing 
the remaining pages in half!

This is Binary Search. It is incredibly fast because it literally throws away 
50% of the data every single time you make a guess. 

2. How does the code work?
--------------------------
To slice the array in half mathematically, you need 3 pointers (variables):
- `left` = the very beginning of the section you're searching
- `right` = the very end of the section you're searching
- `mid` = the exact middle of `left` and `right`

You always check the exact `mid` element:
- Did we guess it perfectly? Awesome! Return the `mid` index.
- Is our `mid` element TOO SMALL? Move the `left` pointer just past the `mid`. (Throwing away the left side!)
- Is our `mid` element TOO BIG? Move the `right` pointer just before the `mid`. (Throwing away the right side!)

3. The One Golden Rule:
-----------------------
BINARY SEARCH ONLY WORKS IF THE ARRAY IS COMPLETELY SORTED!
If the array is scrambled like `[9, 1, 5, 2]`, throwing away the left half 
makes zero mathematical sense because the number "1" could be hiding anywhere!

4. Time Complexities:
---------------------
- Best Case: O(1) -> You open the dictionary exactly to "Zebra" on the first try!
- Worst/Average Case: O(log n) -> Because you mercilessly cut the list in half 
  every step, you can search 1,000,000 items in just 20 steps! 
  (By comparison, Linear Search would take 1,000,000 steps!)
"""

def binary_search(arr, target):
    """
    Searches for the target in a completely SORTED array by slicing it in half.
    
    :param arr: A perfectly SORTED List of items (e.g., numbers)
    :param target: The item we are looking for
    :return: The index of the target if found, otherwise -1.
    """
    # 1. Establish our boundaries at the far extremes
    left = 0
    right = len(arr) - 1
    
    # 2. While our boundaries haven't crossed each other completely
    while left <= right:
        # 3. Find the exact middle index
        mid = (left + right) // 2
        
        # 4. Check the exact middle element
        if arr[mid] == target:
            return mid  # Boom! We found it!
            
        elif arr[mid] < target:
            # The middle is TOO SMALL. The target must be on the right side.
            # Throw away the left side by squeezing the left boundary up!
            left = mid + 1
            
        else:
            # The middle is TOO BIG. The target must be on the left side.
            # Throw away the right side by squeezing the right boundary down!
            right = mid - 1
            
    # 5. If the loop ends and boundaries cross, the target does not exist.
    return -1


def demonstrate_binary_search():
    print("--- Binary Search Demonstration ---")
    
    # IMPORTANT: The list MUST be perfectly sorted from lowest to highest!
    my_sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Our SORTED List: {my_sorted_list}\n")
    
    # 1. Let's search for 23
    target1 = 23
    result1 = binary_search(my_sorted_list, target1)
    if result1 != -1:
        print(f"✅ Found {target1} instantly at exact index: {result1}")
    else:
        print(f"❌ Could not find {target1} anywhere in the list.")
        
    # 2. Let's search for 100
    target2 = 100
    result2 = binary_search(my_sorted_list, target2)
    if result2 != -1:
        print(f"✅ Found {target2} at exact index: {result2}")
    else:
        print(f"❌ Could not find {target2} anywhere. It does not exist.")


if __name__ == "__main__":
    demonstrate_binary_search()
