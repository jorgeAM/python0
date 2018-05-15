import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD = [
    'lavadora',
    'secadora',
    'sofa',
    'television',
    'ps4'
]

def random_word():
    id = random.randint(0, len(WORD) - 1)
    return WORD[id]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')

def run():
    print('B I E N V E N I D O')
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word, tries)
        current_letter = input('Escoge una letra: ')
        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 6:
                display_board(hidden_word, tries)
                print('')
                print('AGG TMR, PERDISTE LA PALABRA ERA '+word)
                print('')
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []

        if not '-' in hidden_word:
            print('')
            print('BIEN CRRANO')
            print('')
            break

run()
