#############################################
## TIC tac toe # tic TAC toe # tic tac TOE ##
#############################################

def title():
    '''GAME TITLE'''
    print('\n'*100)
    print('X O X',' '*11,'O X O')
    print('O X O','TIC-TAC-TOE'+' X O X')
    print('X O X',' '*11,'O X O')
    print('\n'*2)

def names():
    '''PLAYERS NAMES'''
    print('This is a game for two players,\nso bring your friend and we\'ll get started\n')
    PLAYER1 = input('- PLAYER1 name = ').capitalize()
    PLAYER2 = input('- PLAYER2 name = ').capitalize()
    return ('0',PLAYER1,PLAYER2)

def player_input():
    '''PLAYER1 SELECTS MARKER OF CHOICE'''
    marker = ''
    while marker != 'X' or marker != 'O':
        marker = input("\n{}, please select your marker of choice ('X' or 'O'): ".format(PLAYER[1])).upper()
        if marker == 'X':
            return ('#','X','O')
        elif marker == 'O':
            return ('#','O','X')
        else:
            print('Invalid character, please try again...')

def introduction():
    '''INTRODUCTION - EXPLANATION'''
    print('\n')
    print('WELCOME {} & {} !!!\n'.format(PLAYER[1].upper(),PLAYER[2].upper()))
    print('{} controls marker {} and {} controls marker {}'.format(PLAYER[1],markers[1],PLAYER[2],markers[2]))
    print('You will be taking turns, placing your marker on a 3x3 board.')
    print('The first player that manages to place 3 consecutive of his/her marker WINS!')
    print('This can be done Horizontally, Vertically and Diagonally\n\n')

def display_board(board):
    '''GRAPHICAL REPRESENTATION OF BOARD'''
    print(' ')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(board[1],board[2],board[3]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(board[4],board[5],board[6]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(board[7],board[8],board[9]))
    print('     |     |     ')
    print('\n')

def choose_first():
    '''RANDOMLY SELECT WHO STARTS'''
    import random
    turns = random.randint(1,2)
    return turns

def place_marker(board, marker, position):
    '''MARKER PLACEMENT'''
    board[position] = marker

def win_check(board, marker):
    '''CHECK FOR WINNING CONDITIONS'''
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))

def space_check(board, position):
    '''CHECK FOR IF SLOT IS EMPTY'''
    num = position
    return board[position] == str(num)

def full_board_check(board):
    '''CHECK FOR IF BOARD IS FULL'''
    board_count = 0
    for i in range(1,10):
        if board[i] == 'X' or board[i] == 'O':
            board_count += 1
    return board_count == 9

def player1_choice(board):
    '''PLAYER1 PLACES MARKER ON SLOT'''
    player_move = 0
    while True:
        try:
            player_move = int(input('Select in which slot (1-9) to place your marker: \n'))
            if player_move < 1 or player_move > 9:
                print('Invalid slot selection...\n')
                continue
            if space_check(board,player_move) == True:
                place_marker(board, markers[1], player_move)
                print('You placed an {} on slot {}\n'.format(markers[1],player_move))
                break
            else:
                print('This slot is taken, try again on an empty slot...\n')
        except:
            print('Invalid character, try again...\n')

def player2_choice(board):
    '''PLAYER2 PLACES MARKER ON SLOT'''
    player_move = 0
    while True:
        try:
            player_move = int(input('Select in which slot (1-9) to place your marker: \n'))
            if player_move < 1 or player_move > 9:
                print('Invalid slot selection...\n')
                continue
            if space_check(board,player_move) == True:
                place_marker(board, markers[2], player_move)
                print('You placed an {} on slot {}\n'.format(markers[2],player_move))
                break
            else:
                print('This slot is taken, try again on an empty slot...\n')
        except:
            print('Invalid character, try again...\n')

def replay():
    '''ASK TO REPLAY THE GAME'''
    retry = ''
    while retry != 'yes' or retry != 'no':
        retry = input('Would you like to try again? "Yes" or "No": ')
        if retry.lower() == 'y':
            title()
            return True
        elif retry.lower() == 'n':
            print('\n'*2+'Game ended, Thank you for playing {} & {}!!'.format(PLAYER[1],PLAYER[2]))
            return False
        else:
            print('Invalid answer. Please try again...')

 #############
 # MAIN CODE #
 #############

title()
PLAYER = names()          # players in the form of list. Use indexing. P1 = PLAYER[1], P2 = PLAYER[2]
markers = player_input()  # markers in the form of list. Use indexing. P1 = markers[1], P2 = markers[2]
introduction()
game_on = True
turns = choose_first()
while game_on:
    # GAME RESET
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)
    while replay:
        # PLAYER1 TURN:
        if turns%2 == 0:
            if not win_check(board,markers[2]):
                print('{} your turn to play...'.format(PLAYER[1]))
                player1_choice(board)
                turns += 1
                print('\n' * 40)
                display_board(board)
            else:
                print('Bravo {}, you just won the game!!\n'.format(PLAYER[2]))
                game_on = replay()
                break
        # PLAYER2 TURN:
        if turns%2 != 0:
            if not win_check(board,markers[1]):
                print('{} your turn to play...'.format(PLAYER[2]))
                player2_choice(board)
                turns += 1
                print('\n' * 40)
                display_board(board)
            else:
                print('Bravo {}, you just won the game!!\n'.format(PLAYER[1]))
                game_on = replay()
                break
        if full_board_check(board):
            print('Full Board. The game ends in DRAW ')
            game_on = replay()
            break
