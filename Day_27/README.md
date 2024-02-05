# Day 27 of 150 days challenge


The `p_strong` function uses regular expressions to check for the presence of uppercase letters, lowercase letters, numeric digits, and special characters in the password. 

The regular expressions used are as follows:
- `[A-Z]`: Matches any uppercase letter
- `[a-z]`: Matches any lowercase letter
- `\d`: Matches any numeric digit
- `[!@#$%^&*(),.?\":{}|<>]`: Matches any of the listed special characters(`all caharacter not listed`)

The function returns `True` if the password meets all the criteria (including the presence of special characters), and `False` otherwise.
