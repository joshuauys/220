"""
Name: Joshua Uys

lab9.py

Tic Tac Toe

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def ask_for_position():
    players_turn_tracker = 0
    if players_turn_tracker % 2 == 0:
        players_turn = "o"

    if players_turn_tracker % 2 == 1:
        players_turn = "x"

    print("Enter position")
    position = eval(input()) - 1
    return position

def find_players_turn():
    players_turn_tracker = 0
    if players_turn_tracker % 2 == 0:
        players_turn = "o"

    if players_turn_tracker % 2 == 1:
        players_turn = "x"

    players_turn_tracker += 1
    return players_turn

def build_board():
    new_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return new_board

def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def is_legal(board, position):
    legal = True

    if board[position] == "x" or board[position] == "o":
        legal = False
        print("illegal")

    return legal

def fill_spot(board, position, character):
    if is_legal(board, position):
        board[position] = find_players_turn()

def winning_game(board):
    won = False

    # horizontals
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        won = True
    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        won = True

    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        won = True
    if board[3] == "o" and board[4] == "o" and board[5] == "o":
        won = True

    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        won = True
    if board[6] == "o" and board[7] == "o" and board[8] == "o":
        won = True

    # verticles
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        won = True
    if board[0] == "o" and board[3] == "o" and board[6] == "o":
        won = True

    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        won = True
    if board[1] == "o" and board[4] == "o" and board[7] == "o":
        won = True

    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        won = True
    if board[2] == "o" and board[5] == "o" and board[8] == "o":
        won = True

    # diagonals
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        won = True
    if board[0] == "o" and board[4] == "o" and board[8] == "o":
        won = True

    if board[2] == "x" and board[4] == "x" and board[6] == "x":
        won = True
    if board[2] == "o" and board[4] == "o" and board[6] == "o":
        won = True

    return won

def game_over(board):
    any_spaces_left = True
    game_is_over = False

    while any_spaces_left:
        for i in range(len(board)):
            if board[i] == 1 or board[i] == 2 or board[i] == 3 or board[i] == 4 or board[i] == 5 or board[i] == 6 or board[i] == 7 or board[i] == 8 or board[i] == 9:
                any_spaces_left = False

    return game_is_over

def get_winner(board):
    winner = "x"

    # horizontals
    if board[0] == "x" or board[1] == "x" or board[2] == "x":
        winner = "x"
    if board[0] == "o" or board[1] == "o" or board[2] == "o":
        winner = "o"

    if board[3] == "x" or board[4] == "x" or board[5] == "x":
        winner = "x"
    if board[3] == "o" or board[4] == "o" or board[5] == "o":
        winner = "o"

    if board[6] == "x" or board[7] == "x" or board[8] == "x":
        winner = "x"
    if board[6] == "o" or board[7] == "o" or board[8] == "o":
        winner = "o"

    # verticles
    if board[0] == "x" or board[3] == "x" or board[6] == "x":
        winner = "x"
    if board[0] == "o" or board[3] == "o" or board[6] == "o":
        winner = "o"

    if board[1] == "x" or board[4] == "x" or board[7] == "x":
        winner = "x"
    if board[1] == "o" or board[4] == "o" or board[7] == "o":
        winner = "o"

    if board[2] == "x" or board[5] == "x" or board[8] == "x":
        winner = "x"
    if board[2] == "o" or board[5] == "o" or board[8] == "o":
        winner = "o"

    # diagonals
    if board[0] == "x" or board[4] == "x" or board[8] == "x":
        winner = "x"
    if board[0] == "o" or board[4] == "o" or board[8] == "o":
        winner = "o"

    if board[2] == "x" or board[4] == "x" or board[6] == "x":
        winner = "x"
    if board[2] == "o" or board[4] == "o" or board[6] == "o":
        winner = "o"

    return winner

def play(board):
    # while winning_game(board) == False:
    while game_over(board) == False:
        print_board(board)
        fill_spot(board, ask_for_position(), find_players_turn())
    if game_over(board):
        print("you have won")
    # if game_over(board):
    #     print("you have won")

play(build_board())

def main():
    pass


if __name__ == '__main__':
    main()