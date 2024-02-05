import re


def p_strong(password):
    # Check length
    if len(password) < 8:
        return False

    uppercase = False
    lowercase = False
    numeric = False
    special_char = False

    # Check for uppercase, lowercase, numeric, and special characters using regular expressions
    if re.search(r"[A-Z]", password):
        uppercase = True
    if re.search(r"[a-z]", password):
        lowercase = True
    if re.search(r"\d", password):
        numeric = True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        special_char = True

    # Return True if all conditions are met
    return uppercase and lowercase and numeric and special_char


# Test the function
password = input("Input password: ")

if p_strong(password):
    print("Password is strong! Good job.")
else:
    print("Password is weak. Please choose a stronger password.")
