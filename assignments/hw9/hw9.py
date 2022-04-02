"""
Name: Joshua Uys
hw9.py

Hang Man

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Text, Entry, Point

def get_words(file_name):
    words_file = open(file_name, "r")
    words_string = words_file.read()
    words_list = words_string.split("\n")
    return(words_list)

# get_words("words.txt")

def get_random_word(words):
    words_count = len(words)
    random_word = words[randint(0, words_count - 1)]
    return (random_word)

# get_random_word(get_words("words.txt"))

def letter_in_secret_word(letter, secret_word):
    secret_letters = []
    secret_word_length = len(secret_word)
    contains_letter = False

    for i in range(secret_word_length):
        secret_letters += secret_word[i]

    for i in range(secret_word_length):
        if letter == secret_letters[i]:
            contains_letter = True

    return (contains_letter)

# letter_in_secret_word("a", get_random_word(get_words("words.txt")))

def already_guessed(letter, guesses):
    guessed_letter = False

    for i in range(len(guesses)):
        if letter == guesses[i]:
            guessed_letter = True

    return (guessed_letter)

# letter_list = ["c", "b", "d"]
# already_guessed("a", letter_list)

def make_hidden_secret(secret_word, guesses):
    secret_word_length = len(secret_word)
    guesses_length = len(guesses)
    hidden_word_list = []

    """
    creates a list of numbers from 0 to the length of the secret word, 
    these numbers will act as positions of the letters of the secret word and guesses
    """
    for i in range(secret_word_length):
        hidden_word_list += str(i)

    # replaces a number of the list with the correct guess at its position in the secret word
    for x in range(secret_word_length):
        current_secret_letter = secret_word[x]
        current_secret_letter_position = x
        for i in range(guesses_length):
            current_guess = guesses[i]
            if letter_in_secret_word(current_guess, current_secret_letter):
                hidden_word_list[current_secret_letter_position] = current_guess

    # converts the list of numbers and found letters to underscores and found letters
    for i in range(len(hidden_word_list)):
        current_position = i
        current_position_string = str(current_position)
        if hidden_word_list[i] == current_position_string:
            hidden_word_list[i] = "_"

    # print("hidden word list:", hidden_word_list)

    hidden_word = "".join(hidden_word_list)

    return hidden_word

# letter_list = ["c", "b", "a"]
# make_hidden_secret(get_random_word(get_words("words.txt")), letter_list)

def won(guessed):
    did_win = False

    if guessed.find("_") == -1:
        did_win = True

    return did_win

# won(make_hidden_secret(get_random_word(get_words("words.txt")), letter_list))

def play_graphics(secret_word):
    letter_list = []

    width = 400
    height = 800
    win = GraphWin("3 Door Game", width, height)



    hidden_word_display = Text(Point(200, 500), make_hidden_secret(get_random_word(get_words("words.txt")), letter_list))
    hidden_word_display.draw(win)

    for i in range(3):
        letter_entry = Entry(Point(200, 700), 20)
        letter_entry.draw(win)

        guessed_letter_pool = Text(Point(200, 300), letter_list)
        guessed_letter_pool.draw(win)

        win.getMouse()

        guessed_letter = letter_entry.getText()
        if guessed_letter != "" :
            letter_list += guessed_letter
            letter_entry.setText("")

    win.getMouse()
    win.close()

# play_graphics(get_random_word(get_words("words.txt")))


def play_command_line(secret_word):
    guessed_list = []
    guessed_remaining = 20
    #correct words do not count against the remaning guesses

    while guessed_remaining > 0:
        current_guess = input("guess a letter:")
        guessed_already = False

        for i in range(len(guessed_list)):
            if current_guess == guessed_list[i]:
                guessed_already = True

        if guessed_already == False:
            guessed_list += current_guess
            guessed_remaining -= 1

        print("already guessed:", guessed_list)
        print("guesses remaining:", guessed_remaining)
        print(make_hidden_secret(secret_word, guessed_list))

        # not correctly assessing if won
        # not correctly assessing if won
        if won(make_hidden_secret(get_random_word(get_words("words.txt")), letter_list)):
            print("Winner")
            print(secret_word)

    if guessed_remaining == 0:
        print("sorry, you did not guess the word.")
        print("The word was", secret_word)

# play_command_line(get_random_word(get_words("words.txt")))

if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
