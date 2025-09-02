import tkinter as tk
from gui import GuessWordGame

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessWordGame(root)
    root.mainloop()