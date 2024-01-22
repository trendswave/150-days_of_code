import json
import getpass

# Load the existing password data from the JSON file


def load_data():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the password data to the JSON file


def save_data(data):
    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

# Add a new password to the data dictionary


def add_password(data):
    website = input("Which Website is the password for : ")
    username = input("Username: ")
    password = getpass.getpass("password: ")
    data[website] = {'username': username, 'password': password}

# View all saved passwords


def view_passwords(data):
    if not data:
        print("No passwords saved.")
    else:
        for website, info in data.items():
            print(f"Website: {website}")
            print(f"Username: {info['username']}")
            print(f"Password: {info['password']}")
            print('-' * 20)


def main():
    # Load the existing password data
    data = load_data()

    while True:
        print("\n Trendswave PManager")
        print("1. View saved Passwords")
        print("2. Add  new Password")
        print("3. exit the program")

        # Prompt the user for their choice
        choice = input("Enter1, 2, or 3: ")

        if choice == '1':
            # View passwords
            view_passwords(data)
        elif choice == '2':
            # Add a new password
            add_password(data)
            # Save the updated data
            save_data(data)
            print("Password saved successfully.")
        elif choice == '3':
            # Quit the program
            print("Exiting... I like passphrase")
            break
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
