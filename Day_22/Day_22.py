def draw_move(board):
	free = list_of_free_fields(board)  # make a list of free fields
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)