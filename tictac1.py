board = [' ' for x in range(10)]

def insertletter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos]==' '

def printBoard(board):
	print('   |   |')
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print('   |   |')
	print('---------------')
	print('   |   |')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('   |   |')
	print('---------------')
	print('   |   |')
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('   |   |')
	print('---------------')

def isWinner(bo,le):
	return(bo[7] ==le and bo[8] == le and bo[9] == le) or(bo[4] ==le and bo[5] == le and bo[6] == le) or	(bo[1] ==le and bo[2] == le and bo[3] == le) or (bo[1] ==le and bo[4] == le and bo[7] == le) or (bo[2] ==le and bo[5] == le and bo[8] == le) or(bo[3] ==le and bo[6] == le and bo[9] == le) or	(bo[1] ==le and bo[5] == le and bo[9] == le) or (bo[7] ==le and bo[5] == le and bo[3] == le)              

def playerMove():
	run = True
	while run:
		move = input('Please enter a position for x (1-9): ')
		try:
			move = int(move)
			if move>0 and move<10:
				if(spaceIsFree(move)):
					run=False
					insertletter('x',move)
				else:
					print('This place is full')
			else:
				print('Please type a number within the range!')
		except:
			print('Please type a number')


def compMove():
	possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x!=0]
	move = 0

	for let in ['o','x']:
		for i in possibleMove:
			boardCopy = board[:]
			boardCopy[i] = let
			if isWinner(boardCopy,let):
				move = i
				return move

	cornerOpen=[]
	for i in possibleMove:
		if i in [1,3,7,9]:
			cornerOpen.append(i)

	if len(cornerOpen)>0:
		move = selectRandom(cornerOpen)
		return move

	if 5 in possibleMove:
		move = 5
		return move

	edgeOpen =[]

	for i in possibleMove:
		if i in [2,4,6,8]:
			edgeOpenOpen.append(i)

	if len(edgeOpen)>0:
		move = selectRandom(edgeOpen)

	return move



def selectRandom(li):
	import random
	ln = len(li)
	r = random.randrange(0,ln)
	return li[r]

def isBoardFull(board):
	if board.count(' ')>1:
		return False
	else:
		return True 

def main():
	print('Tic Tac Toe')
	printBoard(board)

	while not(isBoardFull(board)):
		if not(isWinner(board, 'o')):
			playerMove()
			printBoard(board)
		else:
			print('o WON THE MATCH')
			break

		if not(isWinner(board, 'x')):
			move = compMove()
			if move == 0:
				print('GAME TIE')
			else:
				insertletter('o',move)
				print('Computer place an\'o\' in position',move,':')
				printBoard(board)
		else:
			print('x WON THE MATCH')
			break


	if isBoardFull(board):
		print('GAME TIE')
while True:
	main()
	if(input('Play Again??(y/n):')=='n'):break
	board = [' ' for x in range(10)]

	