import tkinter as tk
from Class.MainPage import *

class MainApp(tk.Tk):
    def __init__(root):
        tk.Tk.__init__(root)
        root.title("Tic Tac Toe")
        root.geometry("700x800")
        root.mainPage = MainPage(root)
        root.button_play_1v1 = tk.Button(root, text = "Play with Friend",height=3,width= 15,font=('Times New Roman bold', 18),relief = 'solid', command=lambda: root.init_game())
        root.button_play_1v1.place(relx=0.5, rely=0.43, anchor=tk.CENTER)
        root.button_play_ai = tk.Button(root, text = "Play with Ai",height=3,width= 15,font=('Times New Roman bold', 18),relief = 'solid', command=lambda: root.init_game(True))
        root.button_play_ai.place(relx=0.5, rely=0.57, anchor=tk.CENTER)
        root.Label12 = tk.Label(root , text = "TIC TAC TOE",font=('Times New Roman bold',20))
        root.Label12.pack()
        

    def init_game(root,type=False):
        root.button_play_1v1.place_forget()
        root.button_play_ai.place_forget()
        root.mainPage.place(relx=0, rely=0 )
        root.mainPage.add_to_page(type)
        root.Label12.pack_forget()

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
