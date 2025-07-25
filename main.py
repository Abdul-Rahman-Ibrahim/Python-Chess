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
bishop_12 = Bishop('B', 1, 2)
id = bishop_12.get_id()

b_pos = bishop_12.position
sqr = board.squares[b_pos]
print(sqr)
board.update_square(id, b_pos)
sqr = board.squares[b_pos]
print(sqr)
sqr_info = bishop_12.move('b', 2)
print(sqr_info)