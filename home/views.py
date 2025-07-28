from django.shortcuts import render, redirect
from django.views.generic import View

from django.http import JsonResponse

import json

from chess import *

board = Board()




def set_up():
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


set_up()

def make_a_move(board, piece, f, r):
    
    # id = piece.ID
    # file, rank = board.get_current_position(piece)
    success, msg = board.move(piece, f, r)
    return success, msg

class HomeView(View):
    def get(self, request):
        return render(request, 'chessboard.html')


class LegalMoveValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        piece = data['piece']
        source = data['source']
        target = data['target']

        

        src_file, src_rank = board.get_file_rank(source)
        trgt_file, trgt_rank = board.get_file_rank(target)

        piece_obj = board.get_square_info(src_file, src_rank)
        if not piece_obj:
            print(f'Can not move an empty square')
            return JsonResponse({'move_valid': False})

        move_status, msg = make_a_move(board, piece_obj, trgt_file, trgt_rank)
        if not move_status:
            print(f'Invalid Move because {msg}')
            return JsonResponse({'move_valid': False})
        
        print(f'Valid move because {msg}')

        return JsonResponse({'move_valid': True})

class ResetView(View):
    def post(self, request):
    
        board.squares = {}
        for file in board.files:
            for rank in board.ranks:
                board.squares[f'{file}{rank}'] = None
        
        board.white_to_move = True

        set_up()
        return redirect('home')


class GetLegalMoveView(View):
    def get(self, request):
        square = request.GET.get('square')
        if not square:
            return JsonResponse([], safe=False)

        pos_obj = board.squares[square]
        if pos_obj:
            legal_moves = board.get_legal_moves(pos_obj)
            return JsonResponse(legal_moves, safe=False)
        return JsonResponse([], safe=False)

        