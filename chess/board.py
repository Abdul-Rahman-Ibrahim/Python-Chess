
class Board:
    def __init__(self) -> None:
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = list(range(1, 9))
        
        self.top_end = [f'{file}8' for file in self.files]
        self.bottom_end = [f'{file}1' for file in self.files]
        self.right_end = [f'h{rank}' for rank in self.ranks]
        self.left_end = [f'a{rank}' for rank in self.ranks]

        self.squares = {}
        for file in self.files:
            for rank in self.ranks:
                self.squares[f'{file}{rank}'] = None

        self.edges = self.top_end + self.bottom_end + self.right_end + self.left_end
        self.set_up_pieces()
    
    def move(self, Piece: type, file: str, rank: int):
        current_file, current_rank = self.get_current_position(Piece)
        scope = Piece.get_scopes(current_file, current_rank)
        if self.is_move_in_scope(scope, file, rank):
            return 'Move may be possible', scope
        return 'Move is not possible', scope
    
    def get_file_rank(self, position: str):
        file = position[0]
        rank = int(position[1])
        return file, rank
    
    def get_current_position(self, Piece: type):
        square = Piece.position
        if square:
            return self.get_file_rank(square)
        return None, None
        # id = Piece.ID
        
        # for square, piece_id in self.squares.items():
        #     if id == piece_id:
        #         return self.get_file_rank(square)
        # return None, None
    
    def is_move_in_scope(self, scope: list, file: str, rank: int):
        return f'{file}{rank}' in scope
    
    def is_square_empty(self, file: str, rank: int):
        if not self.squares[f'{file}{rank}']:
            return True
        return False

    def get_square_info(self, file:str, rank: int):
        return self.squares[f'{file}{rank}']
    

    def remove_pieces(self):
        self.squares = {}
        for file in self.files:
            for rank in self.ranks:
                self.squares[f'{file}{rank}'] = None

    def update_square(self, ID: str, square):
        self.squares[square] = ID
    
    def set_up_pieces(self):
        self.queen1_pos = 'd1'
        self.queen2_pos = 'd8'
        self.squares['d1'] = 'Q_1'
        self.squares['d8'] = 'Q_2'

        self.bishop11_pos = 'f1'
        self.bishop12_pos = 'c1'
        self.bishop21_pos = 'c8'
        self.bishop22_pos = 'f8'
        self.squares['f1'] = 'B_1_1'
        self.squares['c1'] = 'B_1_2'
        self.squares['c8'] = 'B_2_1'
        self.squares['f8'] = 'B_2_2'

        # Rooks
        self.rook11_pos = 'a1'
        self.rook12_pos = 'h1'
        self.rook21_pos = 'a8'
        self.rook22_pos = 'h8'
        self.squares['a1'] = 'R_1_1'
        self.squares['h1'] = 'R_1_2'
        self.squares['a8'] = 'R_2_1'
        self.squares['h8'] = 'R_2_2'

        # Kings
        self.king1_pos = 'e1'
        self.king2_pos = 'e8'
        self.squares['e1'] = 'K_1'
        self.squares['e8'] = 'K_2'

        # Knights
        self.knight11_pos = 'b1'
        self.knight12_pos = 'g1'
        self.knight21_pos = 'g8'
        self.knight22_pos = 'b8'
        self.squares['b1'] = 'N_1_1'
        self.squares['g1'] = 'N_1_2'
        self.squares['g8'] = 'N_2_1'
        self.squares['b8'] = 'N_2_2'

        # White Pawns
        self.pawn11_pos = 'a2'
        self.pawn12_pos = 'b2'
        self.pawn13_pos = 'c2'
        self.pawn14_pos = 'd2'
        self.pawn15_pos = 'e2'
        self.pawn16_pos = 'f2'
        self.pawn17_pos = 'g2'
        self.pawn18_pos = 'h2'
        self.squares['a2'] = 'P_1_1'
        self.squares['b2'] = 'P_1_2'
        self.squares['c2'] = 'P_1_3'
        self.squares['d2'] = 'P_1_4'
        self.squares['e2'] = 'P_1_5'
        self.squares['f2'] = 'P_1_6'
        self.squares['g2'] = 'P_1_7'
        self.squares['h2'] = 'P_1_8'

        # Black Pawns
        self.pawn21_pos = 'a7'
        self.pawn22_pos = 'b7'
        self.pawn23_pos = 'c7'
        self.pawn24_pos = 'd7'
        self.pawn25_pos = 'e7'
        self.pawn26_pos = 'f7'
        self.pawn27_pos = 'g7'
        self.pawn28_pos = 'h7'
        self.squares['a7'] = 'P_2_1'
        self.squares['b7'] = 'P_2_2'
        self.squares['c7'] = 'P_2_3'
        self.squares['d7'] = 'P_2_4'
        self.squares['e7'] = 'P_2_5'
        self.squares['f7'] = 'P_2_6'
        self.squares['g7'] = 'P_2_7'
        self.squares['h7'] = 'P_2_8'


    def is_square_empty(self, file:str, rank: int):
        pass
    
    def get_queen_position(self, color: int):
        if color == 1:
            return self.queen1_pos
        return self.queen2_pos

    def get_king_position(self, color: int):
        if color == 1:
            return self.king1_pos
        return self.king2_pos

    def get_rook_position(self, color: int, OID: int):
        if color == 1:
            if OID == 1:
                return self.rook11_pos
            return self.rook12_pos
        
        if OID == 1:
            return self.rook21_pos
        return self.rook22_pos

    def get_bishop_position(self, color: int, OID: int):
        if color == 1:
            if OID == 1:
                return self.bishop11_pos
            return self.bishop12_pos
        
        if OID == 1:
            return self.bishop21_pos
        return self.bishop22_pos
        

    def get_knight_position(self, color: int, OID: int):
        if color == 1:
            if OID == 1:
                return self.knight11_pos
            return self.knight12_pos
        
        if OID == 1:
            return self.knight21_pos
        return self.knight22_pos
    
    def get_pawn_position(self, color: int, OID: int):
        if color == 1:
            if OID == 1:
                return self.pawn11_pos
            elif OID == 2:
                return self.pawn12_pos
            elif OID == 3:
                return self.pawn13_pos
            elif OID == 4:
                return self.pawn14_pos
            elif OID == 5:
                return self.pawn15_pos       
            elif OID == 6:
                return self.pawn16_pos
            elif OID == 7:
                return self.pawn17_pos
            elif OID == 8:
                return self.pawn18_pos

        if OID == 1:
            return self.pawn21_pos
        elif OID == 2:
            return self.pawn22_pos
        elif OID == 3:
            return self.pawn23_pos
        elif OID == 4:
            return self.pawn24_pos
        elif OID == 5:
            return self.pawn25_pos       
        elif OID == 6:
            return self.pawn26_pos
        elif OID == 7:
            return self.pawn27_pos
        elif OID == 8:
            return self.pawn28_pos
            

    def is_on_edge(self, file: str, rank: int):
        return f'{file}{rank}' in self.edges

    def is_on_top_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.top_end
    
    def is_on_bottom_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.bottom_end

    def is_on_right_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.right_end

    def is_on_left_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.left_end
    

        