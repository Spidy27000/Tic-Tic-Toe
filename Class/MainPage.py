from dataclasses import dataclass
import tkinter as tk
from tkinter import messagebox
from Class.TicTacToe import *
class Board(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self ,master= master)
        self.master = master
        self.ticTacToe = TicTacToe()
        
        # list of buttons having empty text using list comprehension
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self, text="", font=('Arial', 20), width=8, height=4,
                                command=lambda pos = i: self.on_click(pos))
            btn.grid(row=i%3, column=i//3)
            self.buttons.append(btn)
            btn = None
        
    def on_click(self, pos):
        if (not self.ticTacToe.check_valid_move(pos)):
            messagebox.showerror("Error", "Invalid Move")
            return
        self.buttons[pos].config(text=self.ticTacToe.make_move(pos))
        if (self.ticTacToe.check_win()):
            messagebox.showinfo("Tic Tac Toe", "Player " + self.ticTacToe.check_win() + " wins")
            winner = self.ticTacToe.check_win()
            if self.master.player1.char == winner:
                self.master.player1.score += 1
            if self.master.player2.char == winner:
                self.master.player2.score += 1
            self.master.update_score()
            return
        if (self.ticTacToe.check_draw()):
            messagebox.showinfo("Tic Tac Toe", "Draw")
            return

    def switch_player(self):
        if(self.ticTacToe.check_win()):
            self.master.switch_player(self.ticTacToe.check_win())
        else:
            self.master.switch_player("")
        
    def reset_game(self):
        self.ticTacToe.reset()
        for i in range(9):
            self.buttons[i].config(text="")
        self.switch_player()
@dataclass
class Player:
    char: str
    score: int

class MainPage(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self ,master = master)
        self.board = Board(self)
        self.player_1_label = tk.Label(self, text="Player 1: X", font=('Arial', 12))
        self.score_label = tk.Label(self, text="Score: 0 - 0", font=('Arial', 12))
        self.player_2_label = tk.Label(self, text="Player 2: O", font=('Arial', 12))
        self.player1 = Player("X" ,0)
        self.player2 = Player("O" ,0)
        
        self.quit_button = tk.Button(self, text="quit", font=('Arial',12), command= lambda : self.quit())
        self.reset_game_button = tk.Button(self, text="reset", font = ('Arial',12), command= lambda : self.reset_game())

    def add_to_page(self):
        self.player_1_label.grid(row=1, column=0,padx=(10,1))
        self.score_label.grid(row=1, column=1)
        self.player_2_label.grid(row=1, column=2)
        self.board.grid(row=0, column=0, columnspan=3)
        self.quit_button.grid(row=3, column=1,)
        self.reset_game_button.grid(row=2,column=1)
    
    def reset_game(self):
        self.board.reset_game()
        self.update_score()

    def quit(self):
        self.master.quit()
    
    def update_score(self):
        self.score_label.config(text="Score: " + str(self.player1.score) + " - " + str(self.player2.score))
    
    def switch_player(self,winner):
        if self.player1.char  == X_PLAYER:
            self.player1.char= O_PLAYER
            self.player2.char = X_PLAYER
        else:
            self.player1.char = X_PLAYER
            self.player2.char = O_PLAYER
                
        self.player_1_label.config(text="Player 1: " + str(self.player1.char))
        self.player_2_label.config(text="Player 2: " + str(self.player2.char))