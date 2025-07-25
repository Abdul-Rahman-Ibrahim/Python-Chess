class Board:
    def __init__(self) -> None:
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = list(range(1, 9))
        
        self.top_end = [f'{file}8' for file in self.files]
        self.bottom_end = [f'{file}1' for file in self.files]
        self.right_end = [f'h{rank}' for rank in self.ranks]
        self.left_end = [f'a{rank}' for rank in self.ranks]

        self.edges = self.top_end + self.bottom_end + self.right_end + self.left_end
        self.set_up_pieces()

    def remove_pieces(self):
        pass
    
    def set_up_pieces(self):
        self.queen1_pos = 'd1'
        self.queen2_pos = 'd8'

        self.bishop11_pos = 'f1'
        self.bishop12_pos = 'c1'
        self.bishop21_pos = 'c8'
        self.bishop22_pos = 'f8'

        self.rook11_pos = 'a1'
        self.rook12_pos = 'h1'
        self.rook21_pos = 'a8'
        self.rook22_pos = 'h8'

        self.king1_pos = 'e1'
        self.king2_pos = 'e8'

        self.knight11_pos = 'b1'
        self.knight12_pos = 'g1'
        self.knight21_pos = 'g8'
        self.knight22_pos = 'b8'

        self.pawn11_pos = 'a2'
        self.pawn12_pos = 'b2'
        self.pawn13_pos = 'c2'
        self.pawn14_pos = 'd2'
        self.pawn15_pos = 'e2'
        self.pawn16_pos = 'f2'
        self.pawn17_pos = 'g2'
        self.pawn18_pos= 'h2'

        self.pawn21_pos = 'a7'
        self.pawn22_pos = 'b7'
        self.pawn23_pos = 'c7'
        self.pawn24_pos = 'd7'
        self.pawn25_pos = 'e7'
        self.pawn26_pos = 'f7'
        self.pawn27_pos = 'g7'
        self.pawn28_pos = 'h7'

    def get_square_info(self, file:str, rank: int):
        pass

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