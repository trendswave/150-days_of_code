lotteryDraw = [98, 1, 59, 70, 37, 4] #from the organisation

# Initialize the number of matches
matches = 0

# Collect six picks from the user
for _ in range(6):
    user_pick = int(input("Enter a pick: "))
    if user_pick in lotteryDraw:
        matches += 1

# Print the number of matches
print("You matched", matches, "number(s).")

# Check if the user matched more than three numbers
if matches > 3:
    print("Congratulations, you are a lottery master!")
