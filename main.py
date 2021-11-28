HEIGHT = 3
WIDTH = 3
NB_PLAYER = 2

def hasSomeoneWin(board):

	# NEED TO CHECK ONLY FIVE BECAUSE CORNER CAN'T BE 3 ALIGNED
	# IT'S SHADDY BUT I CAN'T FIND A SOLUTION WIHTOUT A CLASS BEING INVOLVED

	# LEFT VERTICAL LINE
	if board[0][0] != ' ' and board[1][0] != ' ' and board[2][0] != ' ':
		if board[0][0] == board[1][0] == board[2][0]: return True

	# MIDDLE VERTICAL LINE
	if board[0][1] != ' ' and board[1][1] != ' ' and board[2][1] != ' ':
		if board[0][1] == board[1][1] == board[2][1]: return True

	# RIGHT VERTICAL LINE
	if board[0][2] != ' ' and board[1][2] != ' ' and board[2][2] != ' ':
		if board[0][2] == board[1][2] == board[2][2]: return True

	# UP HORIZONTAL LINE
	if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ':
		if board[0][0] == board[0][1] == board[0][2]: return True

	# MIDDLE HORIZONTAL LINE
	if board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ':
		if board[1][0] == board[1][1] == board[1][2]: return True

	# DOWN HORIZONTAL LINE
	if board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
		if board[2][0] == board[2][1] == board[2][2]: return True

	return False

def printPickBoard():
	print(" 1 2 3")
	print(" 4 5 6")
	print(" 7 8 9")

def twoDimTicTacToe():
	board = createTwoDimensionBoard(HEIGHT, WIDTH)
	playerPiece = ['O', 'X']
	actualPlayerTurn = 0

	while not hasSomeoneWin(board):
		a=''
		printPickBoard()
		while len(a) != 1 or not a.isdigit() or a == '0':
			a = input("which Case (1-9)")
		a = int(a) - 1
		w = a % WIDTH
		h = int(a / HEIGHT)
		if board[h][w] != ' ':
			actualPlayerTurn -= 1
			continue
		board[h][w] = playerPiece[actualPlayerTurn]
		for row in board:
			print(" ", end="")
			print(*row, sep=" ")
		actualPlayerTurn += 1
		if actualPlayerTurn >= NB_PLAYER:
			actualPlayerTurn = 0

def main():
	twoDimTicTacToe()
	print("Game Done")
	

def createTwoDimensionBoard(height=3, width=3):
	return [[' ' for i in range(width)] for j in range(height)]

# I'M NOT USING IT TOO COMPLEX
def createOneDimensionBoard(height=3, width=3):
	return [' ' for i in range(width * height)]

if __name__ == '__main__':
	main()