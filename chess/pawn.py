from chess import Board

class Pawn(Board):
    def __init__(self, color: int, OID: int) -> None:
        super().__init__()
        self.name = 'P'
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

        self.position = None

    def get_id(self):
        return self.ID

    def get_scopes(self, file: str, rank: int, can_capture=False, en_pessant=False):
        scopes = []
        try:
            if self.color == 1:
                next_rank = self.ranks[self.ranks.index(rank) + 1]
            elif self.color == 2:
                next_rank = self.ranks[self.ranks.index(rank) - 1]
            scopes.append(f'{file}{next_rank}')
        except IndexError:
            pass
        return scopes #empty = promoting