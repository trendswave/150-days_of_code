/**
 * calculateBirthday - Calculates the day of my birthday.
 * @currentYear: The current year.
 * 
 * This function takes the current year as input and calculates the day of your birthday based on a specific formula.
 * The formula involves using the modulus and division operators to perform mathematical operations on the current year.
 * The resulting day value is returned.
 *
 * Return: The day of your birthday.
 */
int calculateBirthday(int currentYear) {
    int birthDay;

    // Calculate the day of your birthday
    birthDay = (currentYear % 100) * 10 + ((currentYear / 100) % 10);

    return birthDay;
}
