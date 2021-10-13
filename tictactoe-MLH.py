global board
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
player="x"

'''To print tic tac toe board'''
def printBoard(board):
    for line in board:
        print(line)

def makemove():
    global player
    x=int(input(player + ",Enter x"))
    y=int(input("Enter y"))
    
    while board[y][x] != " ":
        print("Enter valid box no!!")
        x=int(input(player + ",Enter x"))
        y=int(input("Enter y"))
    
    if player=="x":
        board[y][x]="x"
        player="o"
    else:
        board[y][x]="o"
        player="x"

def iswin():
	global player
	if player=="x":
		p="o"
	else:
		p="x"	
	
	#row
	for x in range(len(board)):
		win=True
		for y in range(len(board)):
			if board[x][y]!=p:
				win=False
				break
		if win:
			return True
	#column
	for x in range(len(board)):
		win=True
		for y in range(len(board)):
			if board[y][x]!=p:
				win=False
				break
		if win:
			return True
	#diagonals
	win=True
	for x in range(len(board)):
			if board[x][x]!=p:
				win=False
				break
	if win:
		return True


	win=True
	for y in range(len(board)):
			if board[y][len(board)-1-y]!=p:
				win=False
				break
	if win:
		return True


	return False

    

def main():
	gamewon = False
	while gamewon == False:
		printBoard(board)
		makemove()
		gamewon = iswin()
   
	print("GameOver")

main()  
