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
