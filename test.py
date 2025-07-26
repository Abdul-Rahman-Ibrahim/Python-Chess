from chess import *



board = Board()

piece = Pawn(2, 1)
board.set_up_piece(piece)
file, rank = board.get_current_position(piece)
print(f'Status of square {file}{rank} on board is {board.squares[f'{file}{rank}'].ID}')
id = piece.ID
print(f'Piece ID is {id}')
print(f'{id} current position is {file}{rank}')
f, r = 'a', 6
print(f'{id} is attempting to move to {f}{r}')
success, info = board.move(piece, f, r)
if success:
    print(f'{id} moved to {f}{r} because {info}')
else:
    print(f'{id} cannot move to {f}{r} because {info}')
print(f'{id} new position is {piece.position}')
print(f'Status of square {file}{rank} on board is {board.squares[f'{file}{rank}']}')
print(f'Status of square {f}{r} on board is {board.squares[f'{f}{r}']}')

print('-----------------------------------------------------')

piece = Rook(2, 1)
board.set_up_piece(piece)
file, rank = board.get_current_position(piece)
print(f'Status of square {file}{rank} on board is {board.squares[f'{file}{rank}'].ID}')
id = piece.ID
print(f'Piece ID is {id}')
print(f'{id} current position is {file}{rank}')
f, r = 'a', 6
print(f'{id} is attempting to move to {f}{r}')
success, info = board.move(piece, f, r)
if success:
    print(f'{id} moved to {f}{r} because {info}')
else:
    print(f'{id} cannot move to {f}{r} because {info}')
print(f'{id} new position is {piece.position}')
print(f'Status of square {file}{rank} on board is {board.squares[f'{file}{rank}']}')
print(f'Status of square {f}{r} on board is {board.squares[f'{f}{r}']}')


