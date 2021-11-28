HEIGHT = 3
WIDTH = 3
NB_PLAYER = 2
TWODIM = True

def hasSomeoneWin(board):

	for h in range(HEIGHT):
		isDiff = False
		last = board[h][0]
		for w in range(WIDTH):
			if board[h][w] != last or board[h][w] ==  ' ':
				isDiff = True
				break
		if not isDiff:
			return True

	for w in range(WIDTH):
		isDiff = False
		last = board[0][w]
		for h in range(HEIGHT):
			if board[h][w] != last or board[h][w] ==  ' ':
				isDiff = True
				break
		if not isDiff:
			return True

	if HEIGHT != WIDTH:
		return False

	isDiff = False
	last = board[0][0]
	for i in range(HEIGHT):
		if board[i][i] != last or board[i][i] ==  ' ':
			isDiff = True
			break
	if not isDiff:
		return True

	isDiff = False
	last = board[0][HEIGHT - 1]
	for i in range(HEIGHT):
		if board[i][HEIGHT - 1 - i] != last or board[i][HEIGHT - 1 - i] ==  ' ':
			isDiff = True
			break
	if not isDiff:
		return True

	return False

def printPickBoard():
	for h in range(HEIGHT):
		print(" ", end="")
		for w in range(WIDTH):
			print(h * WIDTH + w + 1,end=" ")
		print()

def twoDimTicTacToe():
	board = createTwoDimensionBoard(HEIGHT, WIDTH)
	playerPiece = ['O', 'X']
	actualPlayerTurn = 0

	while not hasSomeoneWin(board):
		a=''
		printPickBoard()
		while len(a) != 1 or not a.isdigit() or a == '0':
			a = input("which Case (1-9) -> ")
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