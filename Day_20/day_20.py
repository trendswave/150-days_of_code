def victory_for(board, sgn):
	if sgn == "X":  # First player
		who = 'me'  # The computer
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
