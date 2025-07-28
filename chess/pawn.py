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
        self.can_capture = False

    def get_id(self):
        return self.ID

    def get_direction(self, file:str, rank:int, next_file:str, next_rank:int):
        if self.color == 1:
            return 'TV', self.get_scopes(file, rank)
        return 'BV', self.get_scopes(file, rank)

    def get_scopes(self, file: str, rank: int, can_capture=False, en_pessant=False):
        scopes = []
        initial_move_next_rank = None

        try:
            if self.color == 1:
                next_rank = self.ranks[self.ranks.index(rank) + 1]
                if not self.has_moved:
                    initial_move_next_rank = self.ranks[self.ranks.index(rank) + 2]
                    self.has_moved = True
            elif self.color == 2:
                next_rank = self.ranks[self.ranks.index(rank) - 1]
                if not self.has_moved:
                    initial_move_next_rank = self.ranks[self.ranks.index(rank) - 2]
                    self.has_moved = True
            scopes.append(f'{file}{next_rank}')
            if initial_move_next_rank:
                scopes.append(f'{file}{initial_move_next_rank}')
        except IndexError:
            pass


        return scopes #empty = promoting
    
    def get_capture_scope(self, file: str, rank: int, squares: dict):
        scope = []
        if self.color == 1:
            # top right
            if f'{file}{rank}' not in self.right_end and f'{file}{rank}' not in self.top_end:
                right_file = self.files[self.files.index(file) + 1]
                top_rank = self.ranks[self.ranks.index(rank) + 1]
                piece_object = squares[f'{right_file}{top_rank}']
                print(piece_object, right_file, top_rank)
                if piece_object:
                    if piece_object.color != self.color:
                        scope.append(f'{right_file}{top_rank}')
            
            #top left
            if f'{file}{rank}' not in self.left_end and f'{file}{rank}' not in self.top_end:
                left_file = self.files[self.files.index(file) - 1]
                top_rank = self.ranks[self.ranks.index(rank) + 1]
                piece_object = squares[f'{left_file}{top_rank}']
                print(piece_object, left_file, top_rank)
                if piece_object:
                    if piece_object.color != self.color:
                        scope.append(f'{left_file}{top_rank}')

            return scope
        
        # bottom right
        if f'{file}{rank}' not in self.right_end and f'{file}{rank}' not in self.bottom_end:
            right_file = self.files[self.files.index(file) + 1]
            bottom_rank = self.ranks[self.ranks.index(rank) - 1]
            piece_object = squares[f'{right_file}{bottom_rank}']
            print(piece_object, right_file, bottom_rank)
            if piece_object:
                if piece_object.color != self.color:
                    scope.append(f'{right_file}{bottom_rank}')
        
        #bottom left
        if f'{file}{rank}' not in self.left_end and f'{file}{rank}' not in self.bottom_end:
            left_file = self.files[self.files.index(file) - 1]
            bottom_rank = self.ranks[self.ranks.index(rank) - 1]
            piece_object = squares[f'{left_file}{bottom_rank}']
            print(piece_object, left_file, bottom_rank)
            if piece_object:
                if piece_object.color != self.color:
                    scope.append(f'{left_file}{bottom_rank}')        

        
        return scope



        # #top right
        # if self.color == 1:
        #     if f'{file}{rank}' not in self.right_end and f'{file}{rank}' not in self.top_end:
        #         right_file = self.files[self.files.index(file) + 1]
        #         top_rank = self.ranks[self.ranks.index(rank) + 1]
        #         piece_object = squares[f'{file}{rank}']
        #         print(piece_object, right_file, top_rank)
        #         if piece_object
        # elif self.color == 2:
        #     if f'{file}{rank}' not in self.left_end and f'{file}{rank}' not in self.bottom_end:
        #         right_file = self.files[self.files.index(file) - 1]
        #         top_rank = self.ranks[self.ranks.index(rank) - 1]
        #         piece_object = self.get_square_info(right_file, top_rank)
        #         piece_object = squares[f'{file}{rank}']
        #         print(piece_object, right_file, top_rank)
        #         if piece_object:

