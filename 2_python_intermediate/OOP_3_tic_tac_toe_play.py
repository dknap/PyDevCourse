# tic tac toe - start to play

import OOP_3_tic_tac_toe as Board

print('Start Game:')
player = input('First move (X / O): ')

board = Board.Board(player.upper())

while (not board.check_if_win()) and (not board.check_if_draw()):
    board.show_board()
    x, y = [int(x) for x in input('Enter the coordinates to put X or O: ').split()]
    board.put_to_board(x, y)

board.show_board()
print()
if board.check_if_win():
    if board.get_player() == 'X':
        print('O won!')
    else:
        print('X won!')
else:
    print('Draw!')