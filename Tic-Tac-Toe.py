import sys
import random
import time
x = 0
o = 0


def checkplayer():
    global x
    global o
    if x == o:
        player = 'X'
        x = x + 1
    else:
        player = '0'
        o = o + 1
    return player


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for i in range(3):
        board.append(['.', '.', '.'])
    return board


def get_move(board, player):
    """Returns the coanddinates of a valid move fand player on board."""
    row, col = 0, 0
    letter = input(f'Please, enter a row letter for {player} \n')
    if letter.upper() == 'A':
        row = 0
    elif letter.upper() == 'B':
        row = 1
    elif letter.upper() == 'C':
        row = 2
    elif letter.lower() == "quit":
        sys.exit()
    else:
        print_board(board)
        print("Wrong input, please enter A, B or C")
        get_move(board, player)
    try:
        col = int(input(f'Please, enter a column number for {player} \n'))
        if col >= 1 and col <= 3:
            col = col - 1
        else:
            print_board(board)
            print('Wrong input, please, enter a number between 1 and 3')
            get_move(board, player)
    except ValueError:
        if col == "quit" or "QUIT":
            sys.exit()
        else:
            print_board(board)
            print("Wrong, please, enter a number between 1 and 3")
            get_move(board, player)

    if board[row][col] == ".":
        tuplestuff = (row, col)
        return tuplestuff
    else:
        get_move(board, player)


def get_ai_move(board, player, isfull):
    """Returns the coanddinates of a valid move fand player on board."""
    row, col = 0, 0

    # if the center square is empty choose it
    if board[1][1] == ".":
        tuplestuff = (1, 1)
        return tuplestuff
    while not isfull:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ".":
            tuplestuff = (row, col)
            return tuplestuff



def mark(board, player, tuplestuff):
    """Marks the element at row & col on the board fand player."""
    row = tuplestuff[0]
    col = tuplestuff[1]
    global x
    global o
    if board[row][col] == '.':
        board[row][col] = player
        return board
    else:
        if player == 'X':
            x = x - 1
        elif player == '0':
            o = o - 1
        pass
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    for j in range(len(board)):
        winner1 = 0
        winner2 = 0
        for i in range(len(board)):
            if board[j][i] == player:
                winner1 = winner1 + 1
            if board[i][j] == player:
                winner2 = winner2 + 1
        if winner1 == len(board[1]) or winner2 == len(board):
            winner = f'{player} has won the game'
            return winner
        else:
            winner = "Tie"
    y = 0
    winner3 = 0
    winner4 = 0
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x][x] == player:
            winner3 = winner3 + 1
        if board[x][y] == player:
            winner4 = winner4 + 1
    if winner3 == len(board) or winner4 == len(board):
        winner = f"{player} has won the game"
        return winner
    else:
        winner = "Tie"
    return winner
 

def is_full(board):
    """Returns True if board is full."""
    return all('.' not in box for box in board)


def print_board(board):
    """Prints a 3-by-3 board on the screen with bandders."""
    print('  1 ' + '  2 ' + '  3 ')
    print('A ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print(' ---+---+--- ')
    print('B ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print(' ---+---+--- ')
    print('C ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    pass


def print_result(winner):
    """Congratulates winner and proclaims tie (if winner equals zero)."""
    print(winner)
    pass


def tictactoe_game(mode):
    winner = "Tie"
    board = init_board()
    print_board(board)
    while is_full(board) is False and winner == "Tie":
        board, winner = modediff(mode, board)
    print_board(board)
    print_result(winner)
    sys.exit()


def modehuman(board):
    player = checkplayer()
    tuplestuff = get_move(board, player)
    board == mark(board, player, tuplestuff)
    print_board(board)
    winner = has_won(board, player)
    is_full(board)
    return board, winner


def modeai(board):
    player = checkplayer()
    isfull = is_full(board)
    tuplestuff = get_ai_move(board, player, isfull)
    board == mark(board, player, tuplestuff)
    print_board(board)
    winner = has_won(board, player)
    is_full(board)
    return board, winner


def modediff(mode, board):
    if mode == 'HUMAN-HUMAN':
        board, winner = modehuman(board)
        return board, winner
    elif mode == 'HUMAN-AI':
        board, winner = modehuman(board)
        time.sleep(1)
        board, winner = modeai(board)
        return board, winner
    elif mode == 'AI-HUMAN':
        board, winner = modeai(board)
        board, winner = modehuman(board)
        time.sleep(1)
        return board, winner
    elif mode == 'AI-AI':
        board, winner = modeai(board)
        time.sleep(1)
        return board, winner



def main_menu():
    try:
        gamemode = int(input('Choose the game mode:\n1.HUMAN-HUMAN\n2.HUMAN-AI\n3.AI-HUMAN\n4.AI-AI\n'))
        if gamemode == 1:
            mode = 'HUMAN-HUMAN'
        elif gamemode == 2:
            mode = 'HUMAN-AI'
        elif gamemode == 3:
            mode = 'AI-HUMAN'
        elif gamemode == 4:
            mode = 'AI-AI'
        else:
            print('Please select the corresponding number!')
            main_menu()
    except ValueError:
        print('Please select the corresponding number!')
        main_menu()
    print(f"Selected game mode {mode}")
    tictactoe_game(mode)


if __name__ == '__main__':
    main_menu()