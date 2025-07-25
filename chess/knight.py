from chess import Board


class Knight(Board):
    def __init__(self, name: str, color: int, OID: int) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.OID = OID
        self.ID = f'{self.name}_{self.color}_{self.OID}'

        self.position = self.get_knight_position(self.color, self.OID)

    def get_id(self):
        return self.ID

    def get_top_right_scope(self, file: str, rank: int, file_skip: int, rank_skip: int):
        scopes = []
        next_file = None
        next_rank = None

        if self.is_on_right_end(file, rank):
            return []
        else:

            try:
                tmp_next_file = file
                tmp_next_rank = rank
                for i in range(1, file_skip+1):
                    tmp_next_file = self.files[self.files.index(file) + i]
                    
                    if self.is_on_right_end(tmp_next_file, rank):
                        if i == file_skip:
                            next_file = tmp_next_file
                        break
                    else:
                        if i == file_skip:
                            next_file = tmp_next_file
            except IndexError:
                pass

        if next_file:
            if self.is_on_top_end(next_file, rank):
                return []
            try:
                for i in range(1, rank_skip+1):
                    tmp_next_rank = self.ranks[self.ranks.index(rank) + i]
                    if self.is_on_top_end(next_file, tmp_next_rank):
                        if i == rank_skip:
                            next_rank = tmp_next_rank
                        break
                    else:
                        if i == rank_skip:
                            next_rank = tmp_next_rank
            except IndexError:
                pass

        if next_file and next_rank:
            scopes.append(f'{next_file}{next_rank}')

            
        return scopes

    def get_top_left_scope(self, file: str, rank: int, file_skip: int, rank_skip: int):
        scopes = []
        next_file = None
        next_rank = None

        if self.is_on_left_end(file, rank):
            return []
        else:

            try:
                tmp_next_file = file
                tmp_next_rank = rank
                for i in range(1, file_skip+1):
                    tmp_next_file = self.files[self.files.index(file) - i]
                    
                    if self.is_on_left_end(tmp_next_file, rank):
                        if i == file_skip:
                            next_file = tmp_next_file
                        break
                    else:
                        if i == file_skip:
                            next_file = tmp_next_file
            except IndexError:
                pass

        if next_file:
            if self.is_on_top_end(next_file, rank):
                return []
            try:
                for i in range(1, rank_skip+1):
                    tmp_next_rank = self.ranks[self.ranks.index(rank) + i]
                    if self.is_on_top_end(next_file, tmp_next_rank):
                        if i == rank_skip:
                            next_rank = tmp_next_rank
                        break
                    else:
                        if i == rank_skip:
                            next_rank = tmp_next_rank
            except IndexError:
                pass

        if next_file and next_rank:
            scopes.append(f'{next_file}{next_rank}')

            
        return scopes

    def get_bottom_right_scope(self, file: str, rank: int, file_skip: int, rank_skip: int):
        scopes = []
        next_file = None
        next_rank = None

        if self.is_on_right_end(file, rank):
            return []
        else:

            try:
                tmp_next_file = file
                tmp_next_rank = rank
                for i in range(1, file_skip+1):
                    tmp_next_file = self.files[self.files.index(file) + i]
                    
                    if self.is_on_right_end(tmp_next_file, rank):
                        if i == file_skip:
                            next_file = tmp_next_file
                        break
                    else:
                        if i == file_skip:
                            next_file = tmp_next_file
            except IndexError:
                pass

        if next_file:
            if self.is_on_bottom_end(next_file, rank):
                return []
            try:
                for i in range(1, rank_skip+1):
                    tmp_next_rank = self.ranks[self.ranks.index(rank) - i]
                    if self.is_on_bottom_end(next_file, tmp_next_rank):
                        if i == rank_skip:
                            next_rank = tmp_next_rank
                        break
                    else:
                        if i == rank_skip:
                            next_rank = tmp_next_rank
            except IndexError:
                pass

        if next_file and next_rank:
            scopes.append(f'{next_file}{next_rank}')
     
        return scopes

    def get_bottom_left_scope(self, file: str, rank: int, file_skip: int, rank_skip: int):
        scopes = []
        next_file = None
        next_rank = None

        if self.is_on_left_end(file, rank):
            return []
        else:

            try:
                tmp_next_file = file
                tmp_next_rank = rank
                for i in range(1, file_skip+1):
                    tmp_next_file = self.files[self.files.index(file) - i]
                    
                    if self.is_on_left_end(tmp_next_file, rank):
                        if i == file_skip:
                            next_file = tmp_next_file
                        break
                    else:
                        if i == file_skip:
                            next_file = tmp_next_file
            except IndexError:
                pass

        if next_file:
            if self.is_on_bottom_end(next_file, rank):
                return []
            try:
                for i in range(1, rank_skip+1):
                    tmp_next_rank = self.ranks[self.ranks.index(rank) - i]
                    if self.is_on_bottom_end(next_file, tmp_next_rank):
                        if i == rank_skip:
                            next_rank = tmp_next_rank
                        break
                    else:
                        if i == rank_skip:
                            next_rank = tmp_next_rank
            except IndexError:
                pass

        if next_file and next_rank:
            scopes.append(f'{next_file}{next_rank}')

            
        return scopes

    def get_scopes(self, file: str, rank: int):
        scope = []

        scope = scope + self.get_top_right_scope(file, rank, file_skip=2, rank_skip=1)
        scope = scope + self.get_top_right_scope(file, rank, file_skip=1, rank_skip=2)
        scope = scope + self.get_top_left_scope(file, rank, file_skip=2, rank_skip=1)
        scope = scope + self.get_top_left_scope(file, rank, file_skip=1, rank_skip=2)
        scope = scope + self.get_bottom_right_scope(file, rank, file_skip=2, rank_skip=1)
        scope = scope + self.get_bottom_right_scope(file, rank, file_skip=1, rank_skip=2)
        scope = scope + self.get_bottom_left_scope(file, rank, file_skip=2, rank_skip=1)
        scope = scope + self.get_bottom_left_scope(file, rank, file_skip=1, rank_skip=2)

        
        return scope


