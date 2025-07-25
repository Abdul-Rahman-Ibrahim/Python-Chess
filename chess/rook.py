from chess import Queen

class Rook(Queen):
    def __init__(self, name: str, color: int, OID: int) -> None:
        super().__init__(name, color)
        self.name = name
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

    def get_scopes(self, file: str, rank: int):
        horizontal = self.get_horizontal_scope(file, rank)
        vertical = self.get_vertical_scope(file, rank)        
        scopes = list(horizontal + (vertical))
        return list(dict.fromkeys(scopes))