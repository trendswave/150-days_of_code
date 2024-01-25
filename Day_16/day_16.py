from random import randrange


def show_board(board):
	print("+-------" * 3, "+", sep="")
	for row in range(3):
		print("|       " * 3, "|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3, "|", sep="")
		print("+-------" * 3, "+",sep="")
		# The progress continues tommorrow