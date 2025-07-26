from chess import *



board = Board()
board.set_up_pieces()

piece = Rook(2, 1)
file, rank = board.get_current_position(piece)
id = piece.ID
print(f'Piece ID is {id}')
print(f'{id} current position is {file}{rank}')
f, r = 'd', 7
print(f'{id} is attempting to move to {f}{r}')
success = board.move(piece, f, r)
if success:
    print(f'{id} moved to {f}{r}')
else:
    print(f'{id} cannot move to {f}{r}')
print(f'{id} new position is {piece.position}')
print(f'{id} new position on board is {board.rook21_pos}')
print(f'Status of square {file}{rank} on board is {board.squares[f'{file}{rank}']}')
print(f'Status of square {f}{r} on board is {board.squares[f'{f}{r}']}')


