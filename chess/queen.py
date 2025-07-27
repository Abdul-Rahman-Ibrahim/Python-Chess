from chess import Board

class Queen(Board):

    def __init__(self, color: int) -> None:
        super().__init__()
        self.name = 'Q'
        self.color = color
        self.ID = f'{self.name}_{self.color}'

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
        
        elif f'{next_file}{next_rank}' in self.get_top_right_scope(file, rank):
            return 'TR', self.get_top_right_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_top_left_scope(file, rank):
            return 'TL', self.get_top_left_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_bottom_right_scope(file, rank):
            return 'BR', self.get_bottom_right_scope(file, rank)
        
        elif f'{next_file}{next_rank}' in self.get_bottom_left_scope(file, rank):
            return 'BL', self.get_bottom_left_scope(file, rank)
    
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
    
    def get_top_left_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.top_end or f'{file}{rank}' in self.left_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        while current_pos not in self.left_end and current_pos not in self.top_end:
            try:
                next_file = self.files[self.files.index(file) - 1]
                next_rank = self.ranks[self.ranks.index(rank) + 1]
                file = next_file
                rank = next_rank
                current_pos = f'{next_file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break     
        return scopes

    def get_top_right_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.top_end or f'{file}{rank}' in self.right_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        while current_pos not in self.right_end and current_pos not in self.top_end:
            try:
                next_file = self.files[self.files.index(file) + 1]
                next_rank = self.ranks[self.ranks.index(rank) + 1]
                file = next_file
                rank = next_rank
                current_pos = f'{next_file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break     
        return scopes

    def get_bottom_left_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.bottom_end or f'{file}{rank}' in self.left_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        while current_pos not in self.bottom_end and current_pos not in self.left_end:
            try:
                next_file = self.files[self.files.index(file) - 1]
                next_rank = self.ranks[self.ranks.index(rank) - 1]
                file = next_file
                rank = next_rank
                current_pos = f'{next_file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break     
        return scopes

    def get_bottom_right_scope(self, file: str, rank: int):
        if f'{file}{rank}' in self.bottom_end or f'{file}{rank}' in self.right_end:
            return []
        scopes = []
        current_pos = f'{file}{rank}'
        while current_pos not in self.bottom_end and current_pos not in self.right_end:
            try:
                next_file = self.files[self.files.index(file) + 1]
                next_rank = self.ranks[self.ranks.index(rank) - 1]
                file = next_file
                rank = next_rank
                current_pos = f'{next_file}{next_rank}'
                scopes.append(f'{current_pos}')
            except IndexError:
                break     
        return scopes
    
    def get_scopes(self, file: str, rank: int):
        right_horizontal = self.get_right_horizontal_scope(file, rank)
        left_horizontal = self.get_left_horizontal_scope(file, rank)
        top_vertical = self.get_top_vertical_scope(file, rank)
        bottom_vertical = self.get_bottom_vertical_scope(file, rank)
        top_right = self.get_top_right_scope(file, rank)
        top_left = self.get_top_left_scope(file, rank)
        bottom_left = self.get_bottom_left_scope(file, rank)
        bottom_right = self.get_bottom_right_scope(file, rank)

        scopes = list(right_horizontal + top_vertical + left_horizontal + bottom_vertical+ top_right + top_left + bottom_left + bottom_right)
        return scopes
    
    def move(self, file: str, rank: int):
        pass
