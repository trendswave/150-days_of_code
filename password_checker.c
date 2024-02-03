#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Checks if the password meets the criteria for a strong password.
 *
 * @return True if the password is strong, false otherwise.
 */
bool isStrongPassword(char password[])
{
    int length = strlen(password);

    // Check for minimum length requirement
    if (length < 8)
    {
        return false;
    }
}