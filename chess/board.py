
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
        
        self.white_to_move = True
    
    def move(self, Piece: type, file: str, rank: int):
        if self.is_piece_turn(Piece):
            current_file, current_rank = self.get_current_position(Piece)
            scope = Piece.get_scopes(current_file, current_rank)
            if self.is_move_in_scope(scope, file, rank):
                dir, scope_dir = Piece.get_direction(current_file, current_rank, file, rank)
                print(dir, scope_dir, f'{file}{rank}')
                for pos in scope_dir:
                    tmp_file, tmp_rank = self.get_file_rank(pos)
                    if (tmp_file, tmp_rank) == (file, rank):
                        break
                    pos_object = self.get_square_info(tmp_file, tmp_rank)
                    if not pos_object:
                        continue

                    if pos != f'{file}{rank}':
                        self.reset_white_to_move(Piece)
                        return False, f'Can not jump over opponent piece {pos_object.ID}'

                    if pos_object.color == Piece.color:
                        self.reset_white_to_move(Piece)
                        return False, f'Can not jump over own piece {pos_object.ID}'

                
                pos_object = self.get_square_info(file, rank)
                if not pos_object:
                    self.update_position(Piece, file, rank, current_file, current_rank)
                    return True, pos_object
                self.update_position(Piece, file, rank, current_file, current_rank)
                return True, f'Can capture opponent piece {pos_object.ID}'
            
            self.white_to_move = self.reset_white_to_move(Piece)
            return False, 'Not scope'
        
        return False, f'Not {Piece.color}\'s turn'
    
    def reset_white_to_move(self, Piece: type):
        if Piece.color == 1:
            self.white_to_move = True
        elif Piece.color == 2:
            self.white_to_move = False
    
    def is_piece_turn(self, Piece: type):
        print(Piece.color)
        if self.white_to_move:
            print('White to move')
            if Piece.color == 1:
                self.white_to_move = False
                return True
            return False
        
        
        if Piece.color == 2:
            print('Black to move')
            self.white_to_move = True
            return True
        
        return False
    
    def update_position(self, Piece: type, file: str, rank: int, current_file: str, current_rank: int):
        Piece.position = f'{file}{rank}'
        self.squares[f'{file}{rank}'] = Piece
        self.squares[f'{current_file}{current_rank}'] = None
                                       
    def get_file_rank(self, position: str):
        file = position[0]
        rank = int(position[1])
        return file, rank
    
    def get_current_position(self, Piece: type):
        square = Piece.position
        if square:
            return self.get_file_rank(square)
        return None, None
    
    def is_move_in_scope(self, scope: list, file: str, rank: int):
        return f'{file}{rank}' in scope

    def get_square_info(self, file:str, rank: int):
        return self.squares[f'{file}{rank}']
    
    def set_up_piece(self, Piece: type):
        if Piece.name == 'K':
            if Piece.color == 1:
                self.squares['e1'] = Piece
                Piece.position = 'e1'
            else:
                self.squares['e8'] = Piece
                Piece.position = 'e8'

        elif Piece.name == 'Q':
            if Piece.color == 1:
                self.squares['d1'] = Piece
                Piece.position = 'd1'
            else:
                self.squares['d8'] = Piece
                Piece.position = 'd8'

        elif Piece.name == 'R':
            if Piece.color == 1:
                if Piece.OID == 1:
                    self.squares['h1'] = Piece
                    Piece.position = 'h1'
                else:
                    self.squares['a1'] = Piece
                    Piece.position = 'a1'
            else:
                if Piece.OID == 1:
                    self.squares['a8'] = Piece
                    Piece.position = 'a8'
                else:
                    self.squares['h8'] = Piece
                    Piece.position = 'h8'

        elif Piece.name == 'B':
            if Piece.color == 1:
                if Piece.OID == 1:
                    self.squares['f1'] = Piece
                    Piece.position = 'f1'
                else:
                    self.squares['c1'] = Piece
                    Piece.position = 'c1'
            else:
                if Piece.OID == 1:
                    self.squares['c8'] = Piece
                    Piece.position = 'c8'
                else:
                    self.squares['f8'] = Piece
                    Piece.position = 'f8'

        elif Piece.name == 'N':
            if Piece.color == 1:
                if Piece.OID == 1:
                    self.squares['b1'] = Piece
                    Piece.position = 'b1'
                else:
                    self.squares['g1'] = Piece
                    Piece.position = 'g1'
            else:
                if Piece.OID == 1:
                    self.squares['g8'] = Piece
                    Piece.position = 'g8'
                else:
                    self.squares['b8'] = Piece
                    Piece.position = 'b8'

        elif Piece.name == 'P':
            if Piece.color == 1:
                if Piece.OID == 1:
                    self.squares['a2'] = Piece
                    Piece.position = 'a2'
                elif Piece.OID == 2:
                    self.squares['b2'] = Piece
                    Piece.position = 'b2'
                elif Piece.OID == 3:
                    self.squares['c2'] = Piece
                    Piece.position = 'c2'
                elif Piece.OID == 4:
                    self.squares['d2'] = Piece
                    Piece.position = 'd2'
                elif Piece.OID == 5:
                    self.squares['e2'] = Piece
                    Piece.position = 'e2'
                elif Piece.OID == 6:
                    self.squares['f2'] = Piece
                    Piece.position = 'f2'
                elif Piece.OID == 7:
                    self.squares['g2'] = Piece
                    Piece.position = 'g2'
                else:
                    self.squares['h2'] = Piece
                    Piece.position = 'h2'
            else:
                if Piece.OID == 1:
                    self.squares['a7'] = Piece
                    Piece.position = 'a7'
                elif Piece.OID == 2:
                    self.squares['b7'] = Piece
                    Piece.position = 'b7'
                elif Piece.OID == 3:
                    self.squares['c7'] = Piece
                    Piece.position = 'c7'
                elif Piece.OID == 4:
                    self.squares['d7'] = Piece
                    Piece.position = 'd7'
                elif Piece.OID == 5:
                    self.squares['e7'] = Piece
                    Piece.position = 'e7'
                elif Piece.OID == 6:
                    self.squares['f7'] = Piece
                    Piece.position = 'f7'
                elif Piece.OID == 7:
                    self.squares['g7'] = Piece
                    Piece.position = 'g7'
                else:
                    self.squares['h7'] = Piece
                    Piece.position = 'h7'

        print(f'{Piece.ID} is set up')

    
    def is_on_top_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.top_end
    
    def is_on_bottom_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.bottom_end

    def is_on_right_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.right_end

    def is_on_left_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.left_end
