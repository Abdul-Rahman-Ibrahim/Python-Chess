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