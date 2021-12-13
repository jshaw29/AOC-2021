import functools
class Board:
    board = None
    last_x = None
    last_y = None
    last_sel = None
    has_bingo = False

    def __init__(self, arrs):
        self.board = arrs
    
    def select(self, val):
        if self.board is not None:
            for i, row in enumerate(self.board):
                try:
                    idx = row.index((val,False))
                    self.board[i][idx] = (val,True)
                    self.last_y = i
                    self.last_x = idx
                    self.last_sel = val
                    break
                except Exception as e:
                    pass
    
    def get_board(self):
        return self.board
    
    def check_bingo(self):
        x = self.last_x
        y = self.last_y
        if x is None or y is None:
            return False
        hor = functools.reduce( lambda x,y: x&y ,[x[1] for x in self.board[y]])
        vert = functools.reduce(lambda x,y : x&y,[r[x][1] for r in self.board])
        self.has_bingo = hor or vert
        return hor or vert
    
    def get_bingo(self):
        return self.has_bingo

    def print(self):
        if self.board:
            for row in self.board:
                print(row)
            print()
    
    def get_score(self):
        sum = functools.reduce(lambda x,y: x+y, [x[0] for y in self.board for x in y if x[1] is False])
        print(sum*self.last_sel)
        