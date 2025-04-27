import random

# The Grid class represents the 2D grid for the Game of Life.
# It handles the grid creation, updates, and operations like cell toggling and neighbor counting.
class Grid:
    def __init__(self, rows, cols):
        # Initialize the grid with a given number of rows and columns.
        # rows: number of rows in the grid
        # cols: number of columns in the grid
        self.rows = rows
        self.cols = cols
        # Create an empty grid (initialized with all cells set to 0).
        self.grid = self.create_empty_grid()

    # Creates and returns an empty grid with all cells set to 0 (dead).
    def create_empty_grid(self):
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    # Randomizes the grid by setting each cell to a random state (0 or 1).
    def randomize(self):
        self.grid = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]

    # Clears the grid by resetting all cells to 0 (dead).
    def clear(self):
        self.grid = self.create_empty_grid()

    # Toggles the state of a specific cell at (row, col) between 0 (dead) and 1 (alive).
    # row: row index of the cell to toggle
    # col: column index of the cell to toggle
    def toggle_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # XOR operation toggles between 0 and 1
            self.grid[row][col] ^= 1

    # Counts the number of alive neighbors surrounding a specific cell at (row, col).
    # row: row index of the cell
    # col: column index of the cell
    def count_neighbors(self, row, col):
        count = 0
        # Check all 8 surrounding neighbors (including diagonals)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # Skip the current cell itself
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r][c]  # Add the neighbor's state (0 or 1)
        return count

    # Advances the grid to the next generation using the Game of Life rules.
    def next_generation(self):
        new_grid = self.create_empty_grid()  # Create a new empty grid for the next generation
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)  # Get the number of alive neighbors
                # Apply the Game of Life rules:
                # 1. A live cell with 2 or 3 live neighbors remains alive.
                if self.grid[i][j] == 1 and neighbors in [2, 3]:
                    new_grid[i][j] = 1
                # 2. A dead cell with exactly 3 live neighbors becomes alive.
                elif self.grid[i][j] == 0 and neighbors == 3:
                    new_grid[i][j] = 1
        self.grid = new_grid  # Update the grid with the new generation

    # Inserts a "glider" pattern at the specified starting position (default is (0, 0)).
    # The glider is a small, moving pattern in the Game of Life.
    def insert_glider(self, start_row=0, start_col=0):
        # Glider pattern as a list of relative coordinates from the starting point.
        glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for dr, dc in glider:
            r, c = start_row + dr, start_col + dc
            # Ensure the glider cells are within the grid's bounds
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.grid[r][c] = 1  # Set the cell to alive (1)
