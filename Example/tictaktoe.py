# 게임 판/ 게임 로직
class Game:
    board = [ ['-','-','-'],
              ['-','-','-'],
              ['-','-','-']]
    win = ''
    player = 0
    def Check(self):
        for i in range(0,3):
            if self.board[0][i]==self.board[1][i]==self.board[2][i]!='-':
                    self.win = self.board[0][i]
                    return False
            elif self.board[i][0]==self.board[i][0]==self.board[i][2]!='-':
                    self.win = self.board[i][0]
                    return False
            elif self.board[0][0]==self.board[1][1]==self.board[2][2]!='-':
                    self.win = self.board[0][0]
                    return False
            elif self.board[2][0]==self.board[1][1]==self.board[0][2]!='-':
                    self.win = self.board[1][1]
                    return False
            else:
                    return True
    def Draw_board(self):
        for i in range(0,3):
            print(self.board[i][0], self.board[i][1], self.board[i][2])
    def Put_button(self,button):
        if 0<=int(button[0])<3 and 0<=int(button[1])<3:
            for i in range(0,3):
                for j in range(0,3):
                    if i == int(button[0]) and j ==int(button[1]):
                        if self.board[i][j] == '-':
                            if self.player%2 == 0:
                                    self.board[i][j] = 'O'
                                    self.player+=1
                            else:
                                    self.board[i][j] = 'X'
                                    self.player+=1
                        else:
                            print("이미 놓은 자리에 놓을 수 없습니다.")
        else:
            print("게임판을 벗어납니다.")
    def clean_board(self):
        for i in range(0,3):
            for j in range(0,3):
                self.board[i][j] = '-'

# 게임 실행
def StartGame():
    game = Game()
    check = True
    while check == True:
        game.Draw_board()
        put_button = input("놓을 위치를 선택하세요")
        game.Put_button(put_button)
        check = game.Check()
        if game.player == 9:
            check = False
            game.Draw_board()
            print("무승부입니다.")
        elif check == False:
            game.Draw_board()
            print("{0}가 이겼습니다.".format(game.win))
StartGame()
Continue = True
# 여러번 실행
while Continue == True:
    yes_no = input("계속하시겠습니까?(y/n)")
    if yes_no == "y":
        game = Game()
        game.clean_board()
        StartGame()
    elif yes_no == "n":
        break
