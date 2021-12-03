import os
import keyboard
import signal
import sys
import color as clr

HEIGHT = 3
WIDTH = 3
NB_PLAYER = 2

heightIndex = 0
widthIndex = 0

clearTerminal = lambda : os.system('cls' if os.name == 'nt' else 'clear')

def getEmptySpotNumber(board):
	"""
	Get the number of empty case in the board
	"""

	emptySpot = 0

	for h in range(HEIGHT):
		for w in range(WIDTH):
			if board[h][w] == ' ':
				emptySpot += 1
	return emptySpot

def hasSomeoneWin(board):
	"""
	Check if someone has won on the board
	"""

	if getEmptySpotNumber(board) == 0:
		return True

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

def printBoard(board):
	"""
	Print the TicTacToe on the term.
	"""
	global widthIndex
	global heightIndex

	for h in range(HEIGHT * 2 + 1):
		for w in range(WIDTH * 2 + 1):
			if w % 2 == 0 or h % 2 == 0:
				print('#',end="")
			else:
				print(board[int(h / 2)][int(w / 2)],end="")
		if heightIndex * 2 + 1 == h:
			print(" <- ",end="")
		print()
	str = " " * (widthIndex * 2 + 1) + "^" 
	print(str)
	print()

def leftArrowPress(key):
	"""
	Reduce widthIndex by 1
	"""
	global widthIndex

	if widthIndex - 1 > -1:
		widthIndex -= 1

def rightArrowPress(key):
	"""
	Increase widthIndex by 1
	"""
	global widthIndex

	if widthIndex + 1 < WIDTH:
		widthIndex += 1

def upArrowPress(key):
	"""
	Reduce heightIndex by 1
	"""
	global heightIndex
	
	if heightIndex - 1 > -1:
		heightIndex -= 1

def downArrowPress(key):
	"""
	Increase heightIndex by 1
	"""
	global heightIndex

	if heightIndex + 1 < HEIGHT:
		heightIndex += 1

def isPossiblePlace(board):
	"""
	Check if it's possible to play on the case with current position.
	"""
	global widthIndex
	global heightIndex


	if board[heightIndex][widthIndex] == ' ':
		return True
	return False

def pickCase(board):
	"""
	Loop until a player press space with good case choosen
	"""
	keyboard.on_press_key("gauche", lambda e: leftArrowPress(e))
	keyboard.on_press_key("droite",  lambda e:  rightArrowPress(e))
	keyboard.on_press_key("haut",  lambda e:  upArrowPress(e))
	keyboard.on_press_key("bas",  lambda e: downArrowPress(e))

	key = ''

	while key != 'space' or not isPossiblePlace(board):
		clearTerminal()
		printBoard(board)
		key = keyboard.read_key()
	
	keyboard.unhook_all()

def twoDimTicTacToe():
	"""
	MAIN LOOP OF THE GAME
	"""
	global widthIndex
	global heightIndex

	board = createTwoDimensionBoard(HEIGHT, WIDTH)
	playerPiece = [f"{clr.Red}O{clr.Color_Off}", f"{clr.Blue}X{clr.Color_Off}"]
	actualPlayerTurn = 0

	while not hasSomeoneWin(board):
		a=''
		clearTerminal()
		pickCase(board)
		board[heightIndex][widthIndex] = playerPiece[actualPlayerTurn]
		actualPlayerTurn += 1
		if actualPlayerTurn >= NB_PLAYER:
			actualPlayerTurn = 0
	clearTerminal()
	printBoard(board)

def signalHandler(sig, frame):
	"""
	Handler for signal
	"""
	print("You pressed Ctrl+C")
	sys.exit(0)

def main():
	signal.signal(signal.SIGINT, signalHandler)
	twoDimTicTacToe()
	print("Game Done")
	

def createTwoDimensionBoard(height=3, width=3):
	"""
	Create a array in 2 dimensions fill with ' '
	"""
	return [[' ' for i in range(width)] for j in range(height)]

if __name__ == '__main__':
	main()