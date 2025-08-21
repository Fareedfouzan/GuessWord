import random

word_bank = ["paris","england","singapore","india"]

word = random.choice(word_bank)

guessedWord = ["_"] * len(word)

attempts = 10

while attempts > 0:
  print('\nCurrent Word: ' + ' '.join(guessedWord))
  
  guess = input('Guess a letter: ').lower()

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessedWord[i] = guess
    print("Great guess!")
  else:
    attempts -= 1
    print("Wrong guess! Attempts left: " + str(attempts))

  if '_' not in guessedWord:
    print("\nCongratulations! You guessed the word: " + word)
    break

else:
    print("\nSorry! You ran out of attempts! The final word is: " + word)