import tkinter as tk
from Class.MainPage import *

class MainApp(tk.Tk):
    def __init__(root):
        tk.Tk.__init__(root)
        root.title("Tic Tac Toe")
        root.geometry("700x800")
        root.mainPage = MainPage(root)
        root.button_play = tk.Button(root, text = "Play", command=lambda: root.init_game())
        root.button_play.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def init_game(root):
        root.button_play.place_forget()
        root.mainPage.place(relx=0, rely=0 )
        root.mainPage.add_to_page()
    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()