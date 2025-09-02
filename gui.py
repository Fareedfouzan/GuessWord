from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
import random

class GuessWordGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Word Game")

        self.word_bank = ["paris", "england", "singapore", "india"]
        self.word = random.choice(self.word_bank)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 10

        self.current_word_label = Label(master, text='Current Word: ' + ' '.join(self.guessed_word))
        self.current_word_label.pack()

        self.guess_entry = Entry(master)
        self.guess_entry.pack()

        self.guess_button = Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

        self.attempts_label = Label(master, text='Attempts left: ' + str(self.attempts))
        self.attempts_label.pack()

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, 'end')

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed_word[i] = guess
            self.current_word_label.config(text='Current Word: ' + ' '.join(self.guessed_word))
            if '_' not in self.guessed_word:
                messagebox.showinfo("Congratulations!", "You guessed the word: " + self.word)
                self.master.quit()
        else:
            self.attempts -= 1
            self.attempts_label.config(text='Attempts left: ' + str(self.attempts))
            if self.attempts == 0:
                messagebox.showinfo("Game Over", "Sorry! You ran out of attempts! The final word is: " + self.word)
                self.master.quit()