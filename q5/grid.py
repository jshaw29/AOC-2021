class Grid:
    grid = None
    x_length = None
    y_length = None

    def __init__(self, max_x, max_y):
        grid = []
        self.grid = grid + [0] *(max_x*max_y)
        self.x_length = max_x
        self.y_length = max_y
    
    def add_vector(self, vector, mode='p1'):
        if mode == 'p1':
            return 
        elif mode =='p2':
            return
    
    def print(self):
        if self.grid is None:
            return
        for i in range(0, self.y_length):
            for j in range(0, self.x_length):
                print(self.grid[i*j], end='')
            print()