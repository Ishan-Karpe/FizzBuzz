"""
FizzBuzz is a simple and classic programming game often used to teach basic logic and control flow. The game involves iterating through numbers from 1 up to a specified limit. For each number:

If the number is divisible by 3, the program outputs "Fizz."
If the number is divisible by 7, it outputs "Buzz."
If the number is divisible by both 3 and 7, it outputs "FizzBuzz."
Otherwise, it simply outputs the number in a string format.
This game is an excellent way to practice using loops, conditionals, and modular arithmetic.
"""


# Start by printing the welcome message:

print("Welcome to FizzBuzz!")
from functools import lru_cache


# Now, create a function called fizzbuzz() that takes a single parameter, amount, and follows the rules above"""


amount = int(input("Enter a number: "))
@lru_cache()
def fizzbuzz(amount):
    for i in range(1, amount + 1):

        # the twist
        """Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz"""

        if ("3" in str(i)) and (i % 3 != 0 and i % 7 != 0):
            print("Almost Fizz")
            continue

        elif (i % 3 == 0) and (i % 7 == 0):  # Both
            print("FizzBuzz")
            continue

        elif i % 3 == 0:  # One
            print("Fizz")
            continue

        elif i % 7 == 0:  # One
            print("Buzz")
            continue

        else:
            print(i)  # if none of the above conditions are met, then print the increment.
            continue


    if amount <= 0:
        print("Invalid Value")
        quit()
    print("That's all of the numbers!")

if __name__ == '__main__':
    fizzbuzz(amount)
