def list_of_free_fields(board):
	free = []
	for row in range(3):  # iterate through rows
		for col in range(3):  # iterate through columns
			if board[row][col] not in ['O', 'X']:  # free cell?
				free.append((row, col))  #append new tuple to the list
	return free
