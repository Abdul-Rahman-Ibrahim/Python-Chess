from chess import Board

class Pawn(Board):
    def __init__(self, color: int, OID: int) -> None:
        super().__init__()
        self.name = 'P'
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

        self.has_moved = False

        self.position = None

    def get_id(self):
        return self.ID

    def get_direction(self, file:str, rank:int, next_file:str, next_rank:int, squares):
        if self.color == 1:
            if file == next_file:
                return 'TV', self.get_scopes(file, rank, squares)
            if file < next_file:
                return 'TL', self.get_scopes(file, rank, squares)
            return 'TR', self.get_scopes(file, rank, squares)
        
        if file == next_file:
            return 'BV', self.get_scopes(file, rank, squares)
        
        if file < next_file:
            return 'BL', self.get_scopes(file, rank, squares)
        return 'BR', self.get_scopes(file, rank, squares)

    def get_scopes(self, file: str, rank: int, squares):
        scopes = []
        initial_move_next_rank = None

        try:
            if self.color == 1:
                next_rank = self.ranks[self.ranks.index(rank) + 1]
                if not self.has_moved:
                    initial_move_next_rank = self.ranks[self.ranks.index(rank) + 2]
            elif self.color == 2:
                next_rank = self.ranks[self.ranks.index(rank) - 1]
                if not self.has_moved:
                    initial_move_next_rank = self.ranks[self.ranks.index(rank) - 2]

            if not squares[f'{file}{next_rank}']:
                scopes.append(f'{file}{next_rank}')
            if initial_move_next_rank:
                if not squares[f'{file}{initial_move_next_rank}']:
                    scopes.append(f'{file}{initial_move_next_rank}')
        except IndexError:
            pass

        if self.color == 1:
            # top right
            if f'{file}{rank}' not in self.right_end and f'{file}{rank}' not in self.top_end:
                right_file = self.files[self.files.index(file) + 1]
                top_rank = self.ranks[self.ranks.index(rank) + 1]
                piece_object = squares[f'{right_file}{top_rank}']
                if piece_object:
                    if piece_object.color != self.color:
                        scopes.append(f'{right_file}{top_rank}')
            
            #top left
            if f'{file}{rank}' not in self.left_end and f'{file}{rank}' not in self.top_end:
                left_file = self.files[self.files.index(file) - 1]
                top_rank = self.ranks[self.ranks.index(rank) + 1]
                piece_object = squares[f'{left_file}{top_rank}']
                if piece_object:
                    if piece_object.color != self.color:
                        scopes.append(f'{left_file}{top_rank}')

            return scopes
        
        # bottom right
        if f'{file}{rank}' not in self.right_end and f'{file}{rank}' not in self.bottom_end:
            right_file = self.files[self.files.index(file) + 1]
            bottom_rank = self.ranks[self.ranks.index(rank) - 1]
            piece_object = squares[f'{right_file}{bottom_rank}']
            if piece_object:
                if piece_object.color != self.color:
                    scopes.append(f'{right_file}{bottom_rank}')
        
        #bottom left
        if f'{file}{rank}' not in self.left_end and f'{file}{rank}' not in self.bottom_end:
            left_file = self.files[self.files.index(file) - 1]
            bottom_rank = self.ranks[self.ranks.index(rank) - 1]
            piece_object = squares[f'{left_file}{bottom_rank}']
            if piece_object:
                if piece_object.color != self.color:
                    scopes.append(f'{left_file}{bottom_rank}')        
        
        return scopes
