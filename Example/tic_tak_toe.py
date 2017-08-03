board = [ [-,-,-], [-,-,-], [-,-,-] ]
check = False
win = ''
while check == True:
	Count = 0
	A = input("행 열을 입력하세요")
	Count += 1
	if int(A[0])>=0 & int(A[0])<3 & int(A[1])>=0 & int(A[1])<3:
		for i in range(0,3):
			for j in range(0,3):
				if int(i==A[0]) & int(j==A[1]):
					if Count%2 == 0:
						board[i][j]='O'
					else:
						board[i][j]='X'
		for i in range(0,3):
				print(board[i][0],board[i][1],board[i][2])
		if count == 9:
			print("무승부입니다")
		elif test() == True:
			print("{0}가 이겼습니다".format(win))	

	else: 
		print("게임판을 벗어납니다")
		for i in range(0,3):
			for j in range(0,3):
				print(board[i][j])		
	
def test():
	for i in range(0,3):
		if board[i][0] == board[i][1] == board[i][2]:
			win = board[i][0]
			return True
		elif board[0][i] == board[1][i] == board[2][i]:
			win = board[0][i]
			return True
		elif board[0][0] == board[1][1] == board[2][2]:
			win = board[0][0]
			return True
		elif board[2][0] == board[1][1] == board[0][2]:
			win = board[2][0]
			return True
		else:
			return False