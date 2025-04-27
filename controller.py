import json
from tkinter import filedialog

class GameController:
    def __init__(self, grid):
        self.grid = grid
        self.running = False
        self.speed = 200

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def step(self):
        self.grid.next_generation()

    def clear(self):
        self.grid.clear()

    def randomize(self):
        self.grid.randomize()

    def save_grid(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.grid.grid, file)

    def load_grid(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                loaded_grid = json.load(f)
                self.grid.grid = loaded_grid

    def insert_glider(self):
        self.grid.insert_glider()


