def print_file_contents(file_path):
    """
    Reads a UTF8 text file and prints its contents to stdout.

    Args:
        file_path (str): The path to the text file.

    Returns:
        None
    """
    try:
        # Open the file with the specified file path in read mode, using UTF8 encoding
        with open(file_path, 'r', encoding='utf8') as file:
            # Iterate over each line in the file
            for line in file:
                # Print each line to stdout without adding an extra newline character
                print(line, end='')
    except FileNotFoundError:
        # Handle the case when the file is not found
        print("File not found.")
    except PermissionError:
        # Handle the case when there is a permission error
        print("Permission denied.")


# Example usage
print_file_contents('path/to/file.txt')
