def matrix_intgr(matrix=[[]]):
    formatted_matrix = ""
    
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each cell in the row
        for cell in range(len(row)):
            # Determine the end character based on whether the cell is the last in the row
            end_char = ' ' if cell + 1 != len(row) else ''
            # Concatenate the formatted integer value with the specified end character
            formatted_matrix += '{:d}{}'.format(row[cell], end_char)
        # Move to the next line after formatting all cells in the current row
        formatted_matrix += '\n'

    return formatted_matrix

# Example Usage
matrix_number_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
formatted_result = matrix_intgr(matrix_number_input)

# Print the formatted matrix
print(formatted_result)
