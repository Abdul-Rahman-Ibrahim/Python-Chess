from chess import Board

class Queen(Board):

    def __init__(self, name: str, color: int) -> None:
        """
        W--> for white
        B --> for black
        """
        super().__init__()
        self.name = name
        self.color = color
        self.ID = f'{self.name}_{self.color}'
        

    def get_horizontal_scope(self, file: str, rank: int):
        scopes = []
        for rnk in self.ranks:
            if rnk == rank:
                continue
            scopes.append(f'{file}{rnk}')
        return scopes
    
    def get_vertical_scope(self, file: str, rank: int):
        scopes = []
        for fl in self.files:
            if fl == file:
                continue
            scopes.append(f'{fl}{rank}')
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
        horizontal = self.get_horizontal_scope(file, rank)
        vertical = self.get_vertical_scope(file, rank)
        top_right = self.get_top_right_scope(file, rank)
        top_left = self.get_top_left_scope(file, rank)
        bottom_left = self.get_bottom_left_scope(file, rank)
        bottom_right = self.get_bottom_right_scope(file, rank)
        scopes = list(horizontal + vertical + top_right + top_left + bottom_left + bottom_right)
        return list(dict.fromkeys(scopes))
