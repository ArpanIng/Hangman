import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']


def hangman():
    word_list = ["marvel", "maverick", "baboon", "window", "windows", "hangman"]
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    print(chosen_word)

    display = []
    for _ in range(word_length):
        display.append("_")
    print(display)

    game_is_on = True
    while game_is_on:
        guess = input("Enter your guess: ").lower()
        if guess not in validletter:
            print("Enter a valid character")
        else:
            if guess in display:
                print("Already guessed")

            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            
            if guess not in chosen_word:
                lives -= 1
                print(f"{lives} lives left")
                if lives == 0: 
                    game_is_on = False
                    print("You lose!")
            print(display)

            if "_" not in display:
                game_is_on = False
                print("bingo! You win!")

            print(stages[lives])

name = input("Enter your name: ").title()
print(f"Welcome {name}")
print("-------")
print(f"You have 7 lives to guess the word")

hangman()
