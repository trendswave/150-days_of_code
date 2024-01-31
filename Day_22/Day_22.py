def draw_move(board):
	free = list_of_free_fields(board)  # make a list of free fields
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'
