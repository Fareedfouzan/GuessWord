import random

class GuessWordGame:
    def __init__(self):
        self.word_bank = ["paris", "england", "singapore", "india"]
        self.word = random.choice(self.word_bank)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 10

    def guess_letter(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed_word[i] = letter
            return True
        else:
            self.attempts -= 1
            return False

    def is_word_guessed(self):
        return '_' not in self.guessed_word

    def get_current_state(self):
        return ' '.join(self.guessed_word), self.attempts

    def get_word(self):
        return self.word

    def reset_game(self):
        self.word = random.choice(self.word_bank)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 10