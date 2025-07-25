from chess import *


# files = 'abcdefgh'
# ranks = '12345678'

# piece = Bishop('B', 1, 1)
# for f in files:
#     for r in ranks:
#         print(f'{f}{r}-->{piece.get_scopes(f, int(r))}')

# f = 'a'
# r = '1'
# piece = Queen('queen', 1)
board = Board()
piece = Rook('P', 1, 2)
print(piece.position)
