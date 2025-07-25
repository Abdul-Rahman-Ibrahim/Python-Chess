from chess import *


# files = 'abcdefgh'
# ranks = '12345678'

# piece = Bishop('B', 1, 1)
# for f in files:
#     for r in ranks:
#         print(f'{f}{r}-->{piece.get_scopes(f, int(r))}')


board = Board()
board.set_up_pieces()

piece = Pawn(2, 8)
file, rank = board.get_current_position(piece)
print(piece.ID)
print(f'{file}{rank}')
print(board.move(piece, 'f', 2))

