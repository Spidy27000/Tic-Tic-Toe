from dataclasses import dataclass
import tkinter as tk
from tkinter import messagebox
from Class.Board import *

@dataclass
class Player:
    char : str
    score : int
        
class BoardFrame(tk.Frame):
    def __init__(self, master, is_ai):
        tk.Frame.__init__(self, master = master)
        self.master = master
        self.board = Board()
        self.player1 = Player("X", 0)
        self.player2 = Player("O", 0)
        
        # list of buttons having empty text using list comprehension
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self, text="", font=('Arial', 20), width=8, height=4,relief = 'solid',
                                command=lambda pos = i: self.on_click(pos))
            btn.grid(row=i%3, column=i//3)
            self.buttons.append(btn)
        
    def on_click(self, pos):
        if (not self.board.check_valid_move(pos)):
            messagebox.showerror("Error", "Invalid Move")
            return
        self.buttons[pos].config(text=self.board.make_move(pos))
        if (self.board.check_win()):
            messagebox.showinfo("Tic Tac Toe", "Player " + self.board.check_win() + " wins")
            winner = self.board.check_win()
            if self.player1.char == winner:
                self.player1.score += 1
            if self.player2.char == winner:
                self.player2.score += 1
            self.master.update_label()
            return
        if (self.board.check_draw()):
            messagebox.showinfo("Tic Tac Toe", "Draw")
            return

    def reset_game(self):
        self.board.reset()
        for i in range(9):
            self.buttons[i].config(text="")

        if self.player1.char  == X_PLAYER:
            self.player1.char= O_PLAYER
            self.player2.char = X_PLAYER
        else:
            self.player1.char = X_PLAYER
            self.player2.char = O_PLAYER

class MainPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self ,master = master)
        self.board = BoardFrame(self,False)

        self.player_1_label = tk.Label(self, text=f"Player 1: {self.board.player1.char}", font=('Times New Roman bold', 12))
        self.score_label = tk.Label(self, text="Score: 0 - 0", font=('Times New Roman bold', 12))
        self.player_2_label = tk.Label(self, text=f"Player 2: {self.board.player2.char}", font=('Times New Roman bold', 12))
        
        self.quit_button = tk.Button(self, text="QUIT",width=6, font=('Times New Roman bold',12), relief = 'solid',command= lambda : self.quit())
        self.reset_game_button = tk.Button(self, text="RESET",width=6, font = ('Times New Roman bold',12), relief = 'solid',command= lambda : self.reset_game())

    def add_to_page(self,is_ai):
        self.board.grid(row=3, column=3, columnspan=3,padx=(150,10),pady=(80,10))
        self.player_1_label.grid(row=4, column=3,padx=(150,1),pady=(1,1))
        self.score_label.grid(row=4, column=4,padx=(1,1),pady=(1,1))
        self.player_2_label.grid(row=4, column=5,padx=(1,1),pady=(1,1))
        
        self.reset_game_button.grid(row=5,column=4,padx=(1,1),pady=(1,10))
        self.quit_button.grid(row=6, column=4,padx=(1,1),pady=(1,1))
        
    
    def reset_game(self):
        self.board.reset_game()
        self.update_label()

    def quit(self):
        self.master.quit()
    
    def update_label(self):
        self.score_label.config(text=f"Score: {self.board.player1.score} - {self.board.player2.score}")
        self.player_1_label.config(text=f"Player 1: {self.board.player1.char}")
        self.player_2_label.config(text=f"Player 2: {self.board.player2.char}")
    
