import json
from tkinter import filedialog

# The GameController class manages the state of the game, controlling its lifecycle and interactions with the user.
class GameController:
    def __init__(self, grid):
        # Initialize the controller with a reference to the grid.
        # grid: an object representing the game grid (the GameOfLife grid).
        self.grid = grid
        self.running = False  # A flag to check if the game is running.
        self.speed = 200  # The speed of the game steps (in milliseconds).

    # Start the game by setting the running flag to True.
    def start(self):
        self.running = True

    # Stop the game by setting the running flag to False.
    def stop(self):
        self.running = False

    # Perform one step in the game by calling the next_generation() method on the grid.
    def step(self):
        self.grid.next_generation()

    # Clear the grid, setting all cells to dead (0).
    def clear(self):
        self.grid.clear()

    # Randomize the grid by setting cells to random states (alive or dead).
    def randomize(self):
        self.grid.randomize()

    # Save the current grid state to a JSON file using a file dialog.
    def save_grid(self):
        # Open a save file dialog where the user can choose the location to save the grid file.
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            # Write the grid state (as a JSON) to the selected file.
            with open(file_path, 'w') as file:
                json.dump(self.grid.grid, file)

    # Load a grid state from a JSON file using a file dialog.
    def load_grid(self):
        # Open an open file dialog where the user can choose a grid file to load.
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            # Read the JSON file and load the grid state into the grid.
            with open(file_path, 'r') as f:
                loaded_grid = json.load(f)
                self.grid.grid = loaded_grid  # Update the grid with the loaded state.

    # Insert a "glider" pattern (a small moving pattern) into the grid at a predefined location.
    def insert_glider(self):
        self.grid.insert_glider()  # Call the insert_glider method on the grid to insert the pattern.
