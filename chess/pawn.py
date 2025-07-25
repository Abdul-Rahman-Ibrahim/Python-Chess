from chess import Board

class Pawn(Board):
    def __init__(self, name: str, color: int, OID: int) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

    def get_scopes(self, file: str, rank: int, can_capture=False, en_pessant=False):
        scopes = []
        try:
            next_rank = self.ranks[self.ranks.index(rank) + 1]
            scopes.append(f'{file}{next_rank}')
        except IndexError:
            pass
        return scopes #empty = promoting