# Use a dictionary to represent a Tic Tac Toe board and play

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board():
    print(the_board['top-L'] + '|' + the_board['top-M'] + '|' + the_board['top-R'])
    print('-+-+-')
    print(the_board['mid-L'] + '|' + the_board['mid-M'] + '|' + the_board['mid-R'])
    print('-+-+-')
    print(the_board['low-L'] + '|' + the_board['low-M'] + '|' + the_board['low-R'])


def check_winner(choice):
    # check the rows
    return ((the_board['top-L'] == the_board['top-M'] == the_board['top-R'] == choice) or
            (the_board['mid-L'] == the_board['mid-M'] == the_board['mid-R'] == choice) or
            (the_board['low-L'] == the_board['low-M'] == the_board['low-R'] == choice) or
            (the_board['top-L'] == the_board['mid-M'] == the_board['low-R'] == choice) or
            (the_board['top-R'] == the_board['mid-M'] == the_board['low-L'] == choice) or
            (the_board['top-L'] == the_board['mid-L'] == the_board['low-L'] == choice) or
            (the_board['top-M'] == the_board['mid-M'] == the_board['low-L'] == choice) or
            (the_board['top-R'] == the_board['mid-R'] == the_board['low-R'] == choice))


# Run the game
choice = 'X'

for i in range(9):
    print_board()
    print('Turn for ' + choice + '. Pick a space:')
    space = input()

    the_board[space] = choice

    # check if we have a winner
    if check_winner(choice):
        print_board()
        print(choice + ' has won!')
        break
    elif choice == 'X':
        choice = 'O'
    else:
        choice = 'X'
