import re
regex = re.compile(r'[123]')
matrix = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]
def create_board():
    print(f'*****************\n*   {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}   *\n*  ---|---|---  *\n*   {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}   *\n*  ---|---|---  *\n*   {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}   *\n*****************')
def player_input(player):
    print(f'Player {player}\'s turn...')
    while True:
        row = input("Enter row: ")
        column = input("Enter column: ")
        if regex.search(row) and regex.search(column):
            break
    row = int(row)
    column = int(column)
    matrix[row-1][column-1] = player
def check_win():
    for horizontal in matrix:
        if horizontal == ['X','X','X']:
            print('X wins!')
            return False
        elif horizontal == ['O','O','O']:
            print('O wins!')
            return False
    vertical = []
    for li in range(0, len(matrix[0])):
        for char in range(0, len(matrix)):
            vertical.append(matrix[char][li])
        if vertical == ['X','X','X']:
            print('X wins!')
            return False
        elif vertical == ['O','O','O']:
            print('O wins!')
            return False
        else:
            vertical = []
    if matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X' or matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X':
            print('X wins!')
            return False
    if matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O' or matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O':
            print('O wins!')
            return False
    empty = ' '
    test = []
    for li in matrix:
        for char in li:
            test.append(char)
    if empty in test:
        pass
    else:
        print('It\'s a tie!')
        return False
    
    return True

def play():
    while check_win():
        create_board()
        player_input("X")
        create_board()
        if check_win() == False:
            break
        player_input("O")
        create_board()
        check_win()

play()