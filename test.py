"""
Chess Piece IDs assigned based on where each piece starts on the board:

Kings:
- king_1  -> White King
- king_2  -> Black King

Queens:
- queen_1 -> White Queen
- queen_2 -> Black Queen

Rooks:
- rook_1_1 -> White Rook on h1
- rook_1_2 -> White Rook on a1
- rook_2_1 -> Black Rook on a8
- rook_2_2 -> Black Rook on h8

Bishops:
- bishop_1_1 -> White Bishop on f1
- bishop_1_2 -> White Bishop on c1
- bishop_2_1 -> Black Bishop on c8
- bishop_2_2 -> Black Bishop on f8

Knights:
- knight_1_1 -> White Knight on b1
- knight_1_2 -> White Knight on g1
- knight_2_1 -> Black Knight on g8
- knight_2_2 -> Black Knight on b8

Pawns:
- pawn_1_1 -> White Pawn on a2
- pawn_1_2 -> White Pawn on b2
- pawn_1_3 -> White Pawn on c2
- pawn_1_4 -> White Pawn on d2
- pawn_1_5 -> White Pawn on e2
- pawn_1_6 -> White Pawn on f2
- pawn_1_7 -> White Pawn on g2
- pawn_1_8 -> White Pawn on h2

- pawn_2_1 -> Black Pawn on a7
- pawn_2_2 -> Black Pawn on b7
- pawn_2_3 -> Black Pawn on c7
- pawn_2_4 -> Black Pawn on d7
- pawn_2_5 -> Black Pawn on e7
- pawn_2_6 -> Black Pawn on f7
- pawn_2_7 -> Black Pawn on g7
- pawn_2_8 -> Black Pawn on h7

"""


from chess import *

board = Board()

king_1 = King(1)
king_2 = King(2)

queen_1 = Queen(1)
queen_2 = Queen(2)

rook_1_1 = Rook(1, 1)
rook_1_2 = Rook(1, 2)
rook_2_1 = Rook(2, 1)
rook_2_2 = Rook(2, 2)

bishop_1_1 = Bishop(1, 1)
bishop_1_2 = Bishop(1, 2)
bishop_2_1 = Bishop(2, 1)
bishop_2_2 = Bishop(2, 2)

knight_1_1 = Knight(1, 1)
knight_1_2 = Knight(1, 2)
knight_2_1 = Knight(2, 1)
knight_2_2 = Knight(2, 2)

pawn_1_1 = Pawn(1, 1)
pawn_1_2 = Pawn(1, 2)
pawn_1_3 = Pawn(1, 3)
pawn_1_4 = Pawn(1, 4)
pawn_1_5 = Pawn(1, 5)
pawn_1_6 = Pawn(1, 6)
pawn_1_7 = Pawn(1, 7)
pawn_1_8 = Pawn(1, 8)

pawn_2_1 = Pawn(2, 1)
pawn_2_2 = Pawn(2, 2)
pawn_2_3 = Pawn(2, 3)
pawn_2_4 = Pawn(2, 4)
pawn_2_5 = Pawn(2, 5)
pawn_2_6 = Pawn(2, 6)
pawn_2_7 = Pawn(2, 7)
pawn_2_8 = Pawn(2, 8)


board.set_up_piece(king_1)
board.set_up_piece(king_2)

board.set_up_piece(queen_1)
board.set_up_piece(queen_2)

board.set_up_piece(rook_1_1)
board.set_up_piece(rook_1_2)
board.set_up_piece(rook_2_1)
board.set_up_piece(rook_2_2)

board.set_up_piece(bishop_1_1)
board.set_up_piece(bishop_1_2)
board.set_up_piece(bishop_2_1)
board.set_up_piece(bishop_2_2)

board.set_up_piece(knight_1_1)
board.set_up_piece(knight_1_2)
board.set_up_piece(knight_2_1)
board.set_up_piece(knight_2_2)

board.set_up_piece(pawn_1_1)
board.set_up_piece(pawn_1_2)
board.set_up_piece(pawn_1_3)
board.set_up_piece(pawn_1_4)
board.set_up_piece(pawn_1_5)
board.set_up_piece(pawn_1_6)
board.set_up_piece(pawn_1_7)
board.set_up_piece(pawn_1_8)

board.set_up_piece(pawn_2_1)
board.set_up_piece(pawn_2_2)
board.set_up_piece(pawn_2_3)
board.set_up_piece(pawn_2_4)
board.set_up_piece(pawn_2_5)
board.set_up_piece(pawn_2_6)
board.set_up_piece(pawn_2_7)
board.set_up_piece(pawn_2_8)

print('------------------------------------------------\n')

def make_a_move(board, piece, f, r):
    
    id = piece.ID
    file, rank = board.get_current_position(piece)
    print(f'{id} current position is {file}{rank}')
    print(f'{id} moving to {f}{r}')
    success, msg = board.move(piece, f, r)
    if success:
        success = 'Succesful'
    else:
        success = 'Failure'
    print(f'{id} moving to {f}{r} is {success} because {msg}')
    print(f'{id} new position is {board.get_current_position(piece)}')
    print(f'Status of {f}{r} is {board.get_square_info(f, r)}')
    print(f'Status of {file}{rank} is {board.get_square_info(file, rank)}')
    print('------------------------------------------------\n')


# files = 'abcdefgh'
# ranks = '12345678'
# piece = Rook(1,1)
# for f in files:
#     for r in ranks:
#         print(piece.get_scopes(f, int(r)))


# Play
# make_a_move(board, pawn_2_5, 'e', 6)
# make_a_move(board, pawn_2_5, 'e', 6)
# make_a_move(board, pawn_2_5, 'e', 4)


make_a_move(board, pawn_1_5, 'e', 4)
make_a_move(board, pawn_2_5, 'e', 6)
make_a_move(board, queen_1, 'f', 3)
make_a_move(board, pawn_2_5, 'e', 7)
make_a_move(board, pawn_2_5, 'e', 5)


make_a_move(board, queen_1, 'f', 7)
make_a_move(board, queen_1, 'f', 7)
# make_a_move(board, pawn_2_5, 'e', 6)


