from chess import Board

class Rook(Board):
    def __init__(self, color: int, OID: int) -> None:
        super().__init__()
        self.name = 'R'
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

        self.position = None
    def get_id(self):
        return self.ID

    def get_direction(self, file:str, rank:int, next_file:str, next_rank:int):
        
        if f'{next_file}{next_rank}' in self.get_right_horizontal_scope(file, rank):
            return 'RH', self.get_right_horizontal_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_left_horizontal_scope(file, rank):
            return 'LH', self.get_left_horizontal_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_top_vertical_scope(file, rank):
            return 'TV', self.get_top_vertical_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_bottom_vertical_scope(file, rank):
            return 'BV', self.get_bottom_vertical_scope(file, rank)

    def get_right_horizontal_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.right_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        next_file = file
        while current_pos not in self.right_end: 
            try:
                next_file = self.files[self.files.index(next_file) + 1]
                current_pos = f'{next_file}{rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break
        return scopes

    def get_left_horizontal_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.left_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        next_file = file
        while current_pos not in self.left_end: 
            try:
                next_file = self.files[self.files.index(next_file) - 1]
                current_pos = f'{next_file}{rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break
        return scopes

    def get_top_vertical_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.top_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        next_rank = rank
        while current_pos not in self.top_end: 
            try:
                next_rank = self.ranks[self.ranks.index(next_rank) + 1]
                current_pos = f'{file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break
        return scopes

    def get_bottom_vertical_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.bottom_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        next_rank = rank
        while current_pos not in self.bottom_end: 
            try:
                next_rank = self.ranks[self.ranks.index(next_rank) - 1]
                current_pos = f'{file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break
        return scopes


    def get_scopes(self, file: str, rank: int):
        right_horizontal = self.get_right_horizontal_scope(file, rank)
        left_horizontal = self.get_left_horizontal_scope(file, rank)
        top_vertical = self.get_top_vertical_scope(file, rank)
        bottom_vertical = self.get_bottom_vertical_scope(file, rank)
        scopes = right_horizontal + left_horizontal + top_vertical + bottom_vertical
        return scopes