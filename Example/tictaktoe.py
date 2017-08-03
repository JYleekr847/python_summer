class Game:

    board = [ ['00','01','02'],
              ['10','11','12'],
              ['20','21','22']]
    win = ''

    def Check(self):
        for i in range(0,3):
            if self.board[0][i]==self.board[1][i]==self.board[2][i]:
                    self.win = self.board[0][i]
                    return False
            elif self.board[i][0]==self.board[i][0]==self.board[i][2]:
                    self.win = self.board[i][0]
                    return False
            elif self.board[0][0]==self.board[1][1]==self.board[2][2]:
                    self.win = self.board[0][0]
                    return False
            elif self.board[2][0]==self.board[1][1]==self.board[0][2]:
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
                        if player%2 == 0:
                                self.board[i][j] = 'O'
                        else:
                                self.board[i][j] = 'X'
        else:
            print("게임판을 벗어납니다.")


check = True
game = Game()
player =0
while check == True:
    game.Draw_board()
    put_button = input("놓을 위치를 선택하세요")
    game.Put_button(put_button)
    player +=1
    check = game.Check()
    if player == 9:
        check = False
        game.Draw_board()
        print("{0}가 이겼습니다.".format(game.win))
    elif check == False:
        game.Draw_board()
        print("{0}가 이겼습니다.".format(game.win))
