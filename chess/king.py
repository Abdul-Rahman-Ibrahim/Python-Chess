from chess import Board


class King(Board):
    def __init__(self, color: int) -> None:
        super().__init__()
        self.name = 'K'
        self.color = color
        self.ID = f'{self.name}_{self.color}'

        self.position = None

    def get_id(self):
        return self.ID

    def get_direction(self, file:str, rank:int, next_file:str, next_rank:int):
        
        if f'{next_file}{next_rank}' in self.get_top_right_scope(file, rank):
            return 'TR', self.get_top_right_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_left_scope(file, rank):
            return 'LH', self.get_left_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_right_scope(file, rank):
            return 'RH', self.get_right_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_top_scope(file, rank):
            return 'TV', self.get_top_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_bottom_scope(file, rank):
            return 'BV', self.get_bottom_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_top_left_scope(file, rank):
            return 'TL', self.get_top_left_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_bottom_right_scope(file, rank):
            return 'BR', self.get_bottom_right_scope(file, rank)
        elif f'{next_file}{next_rank}' in self.get_bottom_left_scope(file, rank):
            return 'BL', self.get_bottom_left_scope(file, rank)

    def get_right_scope(self, file: str, rank: int):
        if self.is_on_right_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) + 1]
        return [f'{next_file}{rank}']
    
    def get_top_scope(self, file: str, rank: int):
        if self.is_on_top_end(file, rank):
            return []
        next_rank = self.ranks[self.ranks.index(rank) + 1]
        return [f'{file}{next_rank}']
    
    def get_left_scope(self, file: str, rank: int):
        if self.is_on_left_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) - 1]
        return [f'{next_file}{rank}']
    
    def get_bottom_scope(self, file: str, rank: int):
        if self.is_on_bottom_end(file, rank):
            return []
        next_rank = self.ranks[self.ranks.index(rank) - 1]
        return [f'{file}{next_rank}']
    
    def get_top_right_scope(self, file: str, rank: int):
        if self.is_on_right_end(file, rank) or self.is_on_top_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) + 1]
        next_rank = self.ranks[self.ranks.index(rank) + 1]
        return [f'{next_file}{next_rank}']
    
    def get_top_left_scope(self, file: str, rank: int):
        if self.is_on_left_end(file, rank) or self.is_on_top_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) - 1]
        next_rank = self.ranks[self.ranks.index(rank) + 1]
        return [f'{next_file}{next_rank}']

    def get_bottom_right_scope(self, file: str, rank: int):
        if self.is_on_right_end(file, rank) or self.is_on_bottom_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) + 1]
        next_rank = self.ranks[self.ranks.index(rank) - 1]
        return [f'{next_file}{next_rank}']

    def get_bottom_left_scope(self, file: str, rank: int):
        if self.is_on_left_end(file, rank) or self.is_on_bottom_end(file, rank):
            return []
        next_file = self.files[self.files.index(file) - 1]
        next_rank = self.ranks[self.ranks.index(rank) - 1]
        return [f'{next_file}{next_rank}']
    
    def get_scopes(self, file: str, rank: int):
        scopes = []
        scopes = scopes + self.get_top_scope(file, rank)
        scopes = scopes + self.get_right_scope(file, rank)
        scopes = scopes + self.get_left_scope(file, rank)
        scopes = scopes + self.get_bottom_scope(file, rank)
        scopes = scopes + self.get_top_right_scope(file, rank)
        scopes = scopes + self.get_top_left_scope(file, rank)
        scopes = scopes + self.get_bottom_right_scope(file, rank)
        scopes = scopes + self.get_bottom_left_scope(file, rank)
        return scopes