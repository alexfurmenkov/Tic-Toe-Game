import random

content = ''
test_board = ['#', f'{content}|', f'{content}|', f'{content}|', f'{content}|', f'{content}|', f'{content}|',
              f'{content}|', f'{content}|', f'{content}|']


# печатает
def print_board(board):
    line_1 = f'{board[1]} {board[2]} {board[3]}'
    line_2 = f'{board[4]} {board[5]} {board[6]}'
    line_3 = f'{board[7]} {board[8]} {board[9]}'

    print(line_1)
    print(line_2)
    print(line_3)


# принимает Х или О. Выбирает будет ли игрок играть за крестики или за нолики
def player_input():
    while True:
        player_1_type = input('Player 1. Choose X or O:')
        player_2_type = input('Player 2. Choose X or O:')

        if player_1_type == 'X' or player_1_type == 'O':
            return player_1_type, player_2_type


# вместо клетки подставляет Х или О
def place_marker(board, marker, position):
    board[position] = marker


# проверяет победителя
def win_check(board, marker):
    line_1 = f'{board[1]} {board[2]} {board[3]}'
    line_2 = f'{board[4]} {board[5]} {board[6]}'
    line_3 = f'{board[7]} {board[8]} {board[9]}'

    if line_1 == f'{marker} {marker} {marker}' or line_2 == f'{marker} {marker} {marker}' or line_3 == f'{marker} {marker} {marker}':
        return True
    elif (board[3] == f'{marker}' and board[6] == f'{marker}' and board[9] == f'{marker}') or (board[2] == f'{marker}' and board[5] == f'{marker}' and board[8] == f'{marker}') or (board[1] == f'{marker}' and board[4] == f'{marker}' and board[7] == f'{marker}'):
        return True
    elif (board[3] == f'{marker}' and board[5] == f'{marker}' and board[7] == f'{marker}') or (board[1] == f'{marker}' and board[5] == f'{marker}' and board[9] == f'{marker}'):
        return True


# выбирает кто ходит первый
def choose_first():
    return random.randint(1, 2)


# проверяет на наличие свободного места на поле на той позиции, которую передал игрок
def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


# проверяет заполнена ли доска или нет
def full_check_board(board):
    counter = 0
    for cell in board:
        if cell == 'X' or cell == "O":
            counter += 1
    if counter == (len(board) - 1):
        return True
    else:
        return False


# спрашивает куда будет игрок ходить дальше
def player_choice(board):
    player_position = int(input('Choose next position:'))
    if space_check(board, player_position):
        return player_position
    else:
        print('Position is already chosen')


# спрашивает хочет ли игрок играть снова
def replay():
    again = input('Do you want to play again? Answer \'Yes\' or \'No\':')
    if again == 'Yes':
        return True
    else:
        return False


# .......................................ИГРА.........................................................................
print('Welcome to Tic Tac Toe!')

while True:

    player_types = player_input()
    player_1 = player_types[0]
    player_2 = player_types[1]

    if player_1 == player_2:
        print('Players cannot have tne same type!')
        player_types = player_input()

    while True:
        print_board(test_board)

        print('Player 1:')
        choice = int(player_choice(test_board))

        place_marker(test_board, player_1, choice)

        print_board(test_board)
        if full_check_board(test_board):
            print('Board is full!')
            break

        if win_check(test_board, player_1):
            print('1 won')
            print('\n \n')
            break

        print('Player 2:')
        choice = player_choice(test_board)

        place_marker(test_board, player_2, choice)

        print_board(test_board)

        if win_check(test_board, player_2):
            print('2 won')
            break

    if replay():
        test_board = ['#', f'{content}|', f'{content}|', f'{content}|', f'{content}|', f'{content}|', f'{content}|',
                      f'{content}|', f'{content}|', f'{content}|']
        continue
    else:
        break
