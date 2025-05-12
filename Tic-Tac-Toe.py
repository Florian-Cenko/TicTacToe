import random


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X'
    else:
        return 'O'


def place_maker(board,marker,position):
    board[position] = marker

def space_check(board,position):
    return board[position] == ' '

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

def win_check(board,mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
    (board[3] == mark and board[4] == mark and board[5] == mark) or
    (board[6] == mark and board[7] == mark and board[8] == mark) or
    (board[0] == mark and board[3] == mark and board[6] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[0] == mark and board[4] == mark and board[8] == mark) or
    (board[2] == mark and board[4] == mark and board[6] == mark))


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

def full_board(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

print('Welcome to Tic Tac Toe!')
board = [' '] * 10
while True:
    player1_maker = player_input()
    if player1_maker == 'X':
        player2_maker = 'O'
    else:
        player2_maker = 'X'

    turn = choose_first()
    print(turn + ' goes first!')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(board)
            position = player_choice(board)
            place_maker(board,player1_maker,position)

            if win_check(board,player1_maker):
                print('Congatulations Player 1 you have won the game!')
                display_board(board)
                game_on = False
            else:
                 if full_board(board):
                     display_board(board)
                     print('The game have no winner!')
                     break
                 else:
                     print("Now the player 2 plays")
                     turn = 'Player 2'

        else:
            display_board(board)
            position = player_choice(board)
            place_maker(board, player2_maker, position)
            display_board(board)

            if win_check(board, player2_maker):
                print('Congatulations Player 2 you have won the game!')
                display_board(board)
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print('The game have no winner!')
                    break
                else:
                    print("Now the player 1 plays")
                    turn = 'Player 1'



    if not replay():
        break