"""
RECURSION (EASY EXPLANATION)

1. What is Recursion?
---------------------
Imagine you are standing in a long line, and you desperately want to know 
what numerical position you are in. You can't see the front of the line.

What do you do?
You politely tap the person directly in front of you and ask: "Hey, what position are you in?"
That person doesn't know either! So they tap the person in front of them and ask 
the exact same question.
This aggressively repeats perfectly, person by person, until the question famously 
reaches the very first person in the entire line.

The first person says, "I'm number 1!"
They turn around and tell the second person. The second person excitedly does some 
quick sequential math: "Ah, if they are #1, I must be #2!" and happily passes the 
calculated number back! The answer physically travels like a beautiful domino effect 
all the way back down the line until the person in front of you turns around and 
says, "I'm number 99!"
You instantly know: "Awesome! I must be number 100!"

In programming, Recursion is simply a brilliantly lazy function that CALLS ITSELF 
to solve a slightly smaller piece of the exact same problem, until it hits an 
answer it magically already knows for absolute certain (the "Base Case").

2. The Two Golden Rules of Recursion:
-------------------------------------
If you write a powerful recursive function, it mathematically MUST have exactly two things:
1. The Base Case (The crucial Stopping condition!): The scenario where the function 
   finally immediately knows the answer without desperately asking anyone else 
   (e.g., "I'm the first person in line! I'm strictly #1!"). 
   Without this, the function will endlessly viciously call itself until the computer 
   tragically runs entirely out of memory and violently crashes!
2. The Recursive Case (The active Action): The part where the function physically 
   calls itself with a slightly smaller version of the exact same problem 
   (e.g., "Person immediately in front of me, what is YOUR exact number?").

3. Example: Factorial (5!)
--------------------------
In formal math, `5!` (5 factorial) is strictly `5 * 4 * 3 * 2 * 1`.
But notice the recursive mathematical pattern hidden inside:
`5! = 5 * (4!)`
`4! = 4 * (3!)`
`3! = 3 * (2!)`
`2! = 2 * (1!)`
`1! = 1` (Boom! This is our Base Case! We natively solidly know 1! is just 1. We don't need to ask 0!).

4. Time Complexities:
---------------------
Recursion is deeply conceptually powerful for complex math, but structurally 
it is often identically as fast as a standard boring `while` loop.
(e.g., Recursively passionately calculating a nested factorial takes standard O(n) Time, just like a `for` loop).
However, it takes immensely more physical RAM memory (a dangerous O(n) Space) 
because the computer forcibly has to keep every single "question" paused and famously 
stacked in its memory (The exact "Call Stack") while waiting for the absolute final answer to travel backwards!
"""

def simple_countdown(n):
    """
    A very basic recursive function that mathematically counts gracefully down to zero.
    """
    # 1. BASE CASE THE GOLDEN RULE. When do we aggressively stop?
    if n <= 0:
        print("Blastoff! 🚀")
        return
        
    # 2. ACTION: What physical print do we do right now?
    print(f"{n}...")
    
    # 3. THE RECURSIVE CASE: Call identically the exact same function, but forcefully one step smaller!
    simple_countdown(n - 1)


def calculate_factorial(n):
    """
    A classic recursive function that aggressively computationally returns the factorial of a number.
    """
    # 1. BASE CASE: If n is 1, we violently solidly stop because we mathematically conclusively know 1! is identically 1.
    if n <= 1:
        return 1
        
    # 2. RECURSIVE CASE: Elegantly actively return `n` multiplied by identically the exact same function physically calculating (n-1)
    return n * calculate_factorial(n - 1)


def demonstrate_recursion():
    print("--- 1. Simple Countdown Demonstration ---")
    simple_countdown(5)
    
    print("\n--- 2. Factorial Demonstration ---")
    num = 5
    result = calculate_factorial(num)
    print(f"The mathematical factorial of {num}! is strictly calculated as: {result}")


if __name__ == "__main__":
    demonstrate_recursion()
