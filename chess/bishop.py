from chess import Queen

class Bishop(Queen):
    def __init__(self, name: str, color: int, OID: int) -> None:
        super().__init__(name, color)
        self.name = name
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

    def get_scopes(self, file: str, rank: int):
        top_right = self.get_top_right_scope(file, rank)
        top_left = self.get_top_left_scope(file, rank)
        bottom_left = self.get_bottom_left_scope(file, rank)
        bottom_right = self.get_bottom_right_scope(file, rank)
        scopes = list(top_right + top_left + bottom_left + bottom_right)
        return list(dict.fromkeys(scopes))