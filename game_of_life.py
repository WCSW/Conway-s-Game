class GameOfLife(object):
    def __init__(self,x_dim,y_dim):
        # Create a 2D list (x_dim rows, y_dim columns) filled with 0s (dead cells)
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.life_grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]

    def get_grid(self):
        # Return the current state of the grid
        return self.life_grid

    