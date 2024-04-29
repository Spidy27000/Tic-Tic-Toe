from Class.Consts import *

class TicTacToe:
    def __init__(self):
        self.board =[0 for _ in range(9)]
        self.player = X_PLAYER
    def make_move(self,pos):
        if (self.player == X_PLAYER and self.check_valid_move(pos)):
            self.board[pos] = X_PLAYER
            self.player = O_PLAYER
        elif (self.player == O_PLAYER and self.check_valid_move(pos)):
            self.board[pos] = O_PLAYER
            self.player = X_PLAYER
        return self.board[pos]
    def check_win(self):
        if (self.board[0] == self.board[1] == self.board[2]!= 0):
            return self.board[0]
        elif (self.board[3] == self.board[4] == self.board[5]!= 0):
            return self.board[3]        
        elif (self.board[6] == self.board[7] == self.board[8]!= 0):
            return self.board[6]
        elif (self.board[0] == self.board[3] == self.board[6]!= 0):
            return self.board[0]
        elif (self.board[1] == self.board[4] == self.board[7]!= 0):
            return self.board[1]
        elif (self.board[2] == self.board[5] == self.board[8]!= 0):
            return self.board[2]
        elif (self.board[0] == self.board[4] == self.board[8]!= 0):
            return self.board[0]
        elif (self.board[2] == self.board[4] == self.board[6]!= 0):
            return self.board[2]
        else:
            return 0
    def check_draw(self):
        for i in range(9):
            if (self.board[i] == 0):
                return False
        return True
    def check_valid_move(self,pos):
        if (self.board[pos] == 0):
            return True
        else:
            return False
    def reset(self):
        self.board =[0 for _ in range(9)]
        self.player = X_PLAYER 
