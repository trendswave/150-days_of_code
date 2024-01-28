#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:  # Check if the number is a multiple of both 3 and 5
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:  # Check if the number is a multiple of 3
            tmp_result.append("Fizz")
        elif (i % 5) == 0:  # Check if the number is a multiple of 5
            tmp_result.append("Buzz")
        else:
            # Convert the number to a string and append it to the result list
            tmp_result.append(str(i))
    # Join the elements of the result list with spaces and print the resulting string
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
