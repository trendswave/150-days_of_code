#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Checks if the password meets the criteria for a strong password.
 *
 * @param password The password to be checked.
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

    // Check for presence of uppercase, lowercase, and numeric characters
    bool hasUppercase = false;
    bool hasLowercase = false;
    bool hasNumeric = false;

    for (int i = 0; i < length; i++)
    {
        if (password[i] >= 'A' && password[i] <= 'Z')
        {
            hasUppercase = true;
        }
        else if (password[i] >= 'a' && password[i] <= 'z')
        {
            hasLowercase = true;
        }
        else if (password[i] >= '0' && password[i] <= '9')
        {
            hasNumeric = true;
        }
    }

    return (hasUppercase && hasLowercase && hasNumeric);
}

int main(void)
{
    char password[100];
    printf("Enter your password: ");
    scanf("%s", password);

    if (isStrongPassword(password))
    {
        printf("Password is strong! Good job.\n");
    }
    else
    {
        printf("Password is weak. Please choose a stronger password.\n");
    }

    return 0;
}