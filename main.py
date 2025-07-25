from chess import King


files = 'abcdefgh'
ranks = '12345678'

piece = King()
for f in files:
    for r in ranks:
        print(f'{f}{r}-->{piece.get_scopes(f, int(r))}')

# f = 'a'
# r = 8
# board = Board()
# print(board.is_on_top_end('e', 8))
# queen = Queen()
# print(queen.get_scopes('b', 7))
# bishop = Bishop()
# print(bishop.get_scopes('g', 5))
# piece = King()
# print(f'{f}{r} --> {piece.get_scopes(f, r)}')
