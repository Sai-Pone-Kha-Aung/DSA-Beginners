"""
LINEAR SEARCH (EASY EXPLANATION)

1. What is Linear Search?
-------------------------
Imagine you lose your keys in your house. How do you find them?
You start at the front door, walk into the first room, and look around.
If they aren't there, you walk into the second room and look.
You keep checking every single room, one by one in a straight line, until 
you either find the keys or you've checked the entire house and realize 
they are completely gone.

This exact process is called Linear Search!
In programming, "Linear Search" simply means looking for a specific value 
(like the number 7) inside an array/list by checking every single element 
one-by-one, starting from the very beginning (`index 0`) to the very end.

2. How does the code work?
--------------------------
It's literally just a standard `for` loop!
You loop through the array:
- If `current_item == target_item`, you shout "Found it!" and return its index.
- If the loop naturally finishes scanning the entire array and never found the 
  target, you return `-1` to signal to the computer "It's not here".

3. Time Complexities:
---------------------
- Best Case: O(1) -> You get incredibly lucky and the item is the VERY FIRST 
  thing in the list! You only had to check 1 thing.
- Worst Case: O(n) -> You are very unlucky and the item is the VERY LAST thing 
  in the list (or it's not in the list at all). You had to manually check `n` things.
- Average Case: O(n) -> On average, you have to search through half the list.

4. When to use it?
------------------
Linear Search is extremely simple to write, but it is considered "slow" for 
massive lists (like an array of 1 million users).
However, it is practically the ONLY search algorithm you can use if your list 
is COMPLETELY UNSORTED or scrambled (like `[9, 2, 5, 1, 8]`). 

(Note: If the list is perfectly sorted, there is a much faster trick called 
Binary Search that we can use instead!)
"""

def linear_search(arr, target):
    """
    Searches for the target in the array one by one.
    
    :param arr: List of items (e.g., numbers, strings)
    :param target: The item we are actually looking for
    :return: The exact index of the target if found, otherwise -1.
    """
    # 1. Start at the beginning and check every single room/index
    for index in range(len(arr)):
        
        # 2. Did we find the keys?
        if arr[index] == target:
            return index  # YES! We found it! Return exactly where it is.
            
    # 3. We checked the whole house (the loop fully finished without returning anything).
    return -1


def demonstrate_linear_search():
    print("--- Linear Search Demonstration ---")
    
    my_unsorted_list = [45, 12, 89, 33, 7, 21, 99]
    print(f"Our List: {my_unsorted_list}\n")
    
    # 1. Let's search for 33 (It exists!)
    target1 = 33
    result1 = linear_search(my_unsorted_list, target1)
    if result1 != -1:
        print(f"✅ Found {target1} at exact index: {result1}")
    else:
        print(f"❌ Could not find {target1} anywhere in the list.")
        
    # 2. Let's search for 100 (which doesn't exist!)
    target2 = 100
    result2 = linear_search(my_unsorted_list, target2)
    if result2 != -1:
        print(f"✅ Found {target2} at exact index: {result2}")
    else:
        print(f"❌ Could not find {target2} anywhere in the list. Checked everything!")


if __name__ == "__main__":
    demonstrate_linear_search()
