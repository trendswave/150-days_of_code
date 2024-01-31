from random import randrange


def display_board(board):
	print("+-------" * 3, "+", sep="")
	for row in range(3):
		print("|       " * 3, "|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3, "|", sep="")
		print("+-------" * 3, "+", sep="")


def your_move(board):
	# This is just an assumption
	status = False
	while not status:
		move = input("Enter your move: ")
	    # Check the validity of user's input, range of 1-9
		status = len(move) == 1 and move >= '1' and move <= '9'
		if not status:
		 # Requests for a new input
			print("Wrong move - repeat your input!")
			continue
		# cell's number from 0 to 8
		move = int(move) - 1
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]  # check the selected square
		status = sign not in ['O', 'X']
		if not status:  # it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square


def list_of_free_fields(board):
	free = []
	for row in range(3):  # iterate through rows
		for col in range(3):  # iterate through columns
			if board[row][col] not in ['O', 'X']:  # free cell?
				free.append((row, col))  # append new tuple to the list
	return free


def victory_for(board, sgn):
	if sgn == "X":  # First player
		who = 'me'  # 
	elif sgn == "O":  # Second player
		who = 'you'  # yes - it's our side
	else:
		who = None
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # check column rc
			return who
		if board[rc][rc] != sgn:  # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn:  # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board)  # make a list of free fields
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

