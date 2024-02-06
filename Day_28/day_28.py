import math


def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Prompt the user to enter a number
user_input = int(input("Enter a number: "))
# Check if the number is prime
if prime(user_input):
    print("It is a prime number!")
else:
    print("It is not a prime number.")
