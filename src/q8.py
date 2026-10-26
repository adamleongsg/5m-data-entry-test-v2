"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: The buggy version returns 3 because "n % 2 == 1" checks for odd numbers instead of even numbers. There are three odd numbers (1, 3 and 5) in the list.

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    # your corrected code here
    count = 0
    for n in numbers:
        if n % 2 == 0:      
            count = count + 1
    return count


"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: It checks whether a number is even by testing if the remainder is zero when the number is divided by 2.
"""
