import random

class Grid:
    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def randomize(self):
        self.grid = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]

    def clear(self):
        self.grid = self.create_empty_grid()

    def toggle_cell(self,row,col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] ^= 1

    def count_neighbors(self,row,col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                r,c = row + i, col+j
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r][c]
        return count

    def next_generation(self):
        new_grid = self.create_empty_grid()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i,j)
                if self.grid[i][j] == 1 and neighbors in [2,3]:
                    new_grid[i][j] = 1
                elif self.grid[i][j] == 0 and neighbors == 3:
                    new_grid[i][j] = 1
        self.grid = new_grid

    def insert_glider(self,start_row = 0,start_col = 0):
        glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for dr, dc in glider:
            r, c = start_row + dr, start_col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.grid[r][c] = 1

