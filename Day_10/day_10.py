while True:
    try:
        # Prompt user to enter an integer
        number = int(input("Enter an int number: "))
        print(number/5)  # Perform division operation
        break  # Exit the loop if no exceptions occur
    except ValueError:  # Handle the ValueError exception
        print("Wrong value.")  # Display an error message for incorrect input
    except ZeroDivisionError:  # Handle the ZeroDivisionError exception
        # Display an error message for division by zero
        print("Sorry. I cannot divide by zero.")
    except:  # Handle any other exceptions
        print("I don't know what to do...")  # Display a generic error message
