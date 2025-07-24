
class Board:
    def __init__(self) -> None:
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = list(range(1, 9))
        
        self.top_end = [f'{file}8' for file in self.files]
        self.bottom_end = [f'{file}1' for file in self.files]
        self.right_end = [f'h{rank}' for rank in self.ranks]
        self.left_end = [f'a{rank}' for rank in self.ranks]

        self.edges = self.top_end + self.bottom_end + self.right_end + self.left_end
    
    def is_on_edge(self, file: str, rank: int):
        return f'{file}{rank}' in self.edges

    def is_on_top_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.top_end
    
    def is_on_bottom_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.bottom_end

    def is_on_right_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.right_end

    def is_on_left_end(self, file: str, rank: int):
        return f'{file}{rank}' in self.left_end

        
class Queen(Board):

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


class Bishop(Queen):
    def get_scopes(self, file: str, rank: int):
        top_right = self.get_top_right_scope(file, rank)
        top_left = self.get_top_left_scope(file, rank)
        bottom_left = self.get_bottom_left_scope(file, rank)
        bottom_right = self.get_bottom_right_scope(file, rank)
        scopes = list(top_right + top_left + bottom_left + bottom_right)
        return list(dict.fromkeys(scopes))


class Knight(Board):

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



class Rook(Queen):
    def get_scopes(self, file: str, rank: int):
        horizontal = self.get_horizontal_scope(file, rank)
        vertical = self.get_vertical_scope(file, rank)        
        scopes = list(horizontal + (vertical))
        return list(dict.fromkeys(scopes))


class Pawn(Board):
    def get_scopes(self, file: str, rank: int, can_capture=False, en_pessant=False):
        scopes = []
        try:
            next_rank = self.ranks[self.ranks.index(rank) + 1]
            scopes.append(f'{file}{next_rank}')
        except IndexError:
            pass
        return scopes #empty = promoting


class King(Queen):
    def get_scopes(self, file: str, rank: int):
        pass



    

files = 'abcdefgh'
ranks = '12345678'

piece = Pawn()
for f in files:
    for r in ranks:
        print(f'{f}{r}-->{piece.get_scopes(f, int(r))}')

# f = 'h'
# r = 8 
# # board = Board()
# # print(board.is_on_top_end('e', 8))
# # queen = Queen()
# # print(queen.get_scopes('b', 7))
# # bishop = Bishop()
# # print(bishop.get_scopes('g', 5))
# knight = Knight()
# print(f'{f}{r} --> {knight.get_scopes(f, r)}')

        
