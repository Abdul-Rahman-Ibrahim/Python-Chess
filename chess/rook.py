from chess import Board

class Rook(Board):
    def __init__(self, color: int, OID: int) -> None:
        super().__init__()
        self.name = 'R'
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

        self.position = self.get_rook_position(self.color, self.OID)

    def get_id(self):
        return self.ID

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

    def get_scopes(self, file: str, rank: int):
        horizontal = self.get_horizontal_scope(file, rank)
        vertical = self.get_vertical_scope(file, rank)        
        scopes = list(horizontal + (vertical))
        return list(dict.fromkeys(scopes))