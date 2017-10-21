import random

def choose_random_word():
    f = open('hangman_words.txt', 'r')
    words = f.readlines()

    words = words.split(' ')
    secret_word = random.choice(words)
    return secret_word

def check_guess(guess, secret_word):
    if guess in secret_word:
        return True
    else: 
        return False

def get_guessed_word(letters_guessed, secret_word):
    guessed_word = ''

    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed_word += secret_word[letter]
        else:
            guessed_word += "_ "
    return guessed_word

def get_available_letters(letters_guessed):
    letters_available = ''

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in letters_guessed:
            letters_available += letter
    return letters_available.lower()

def is_guessed(secret_word, letters_guessed):
    count = 0

    for letter in letters_guessed:
        if letter in secret_word:
            count += 1

            if count == len(secret_word):
                return True
            else:
                return False

  def hangman(secret_word):

      letters_guessed = []
      guess_count = 10

      print("Welcome to Hangman!!!")
      print("The secret word is {} letters long. Good Luck :)").format(len(secret_word))
