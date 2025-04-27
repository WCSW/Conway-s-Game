import tkinter as tk

class GameUI:
    def __init__(self, root, grid, controller, theme_manager):
        # Initialize the GameUI object with references to the root, grid, controller, and theme manager
        self.root = root
        self.grid = grid
        self.controller = controller
        self.theme = theme_manager
        self.cell_size = 20  # Set the size of each cell in the grid

        # Setup the user interface elements
        self._setup_ui()

        # Draw the initial grid
        self._draw_grid()

    def _setup_ui(self):
        # Create a Canvas widget to display the grid
        self.canvas = tk.Canvas(
            self.root,
            width=self.grid.cols * self.cell_size,
            height=self.grid.rows * self.cell_size,
            bg=self.theme.get_color("background"),  # Set the background color based on the theme
            highlightthickness=0  # Remove the border highlight
        )
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self._on_canvas_click)  # Bind left mouse click event to a function

        # Create a frame for the buttons
        button_frame = tk.Frame(self.root, bg=self.theme.get_color("background"))
        button_frame.pack()

        # Define the actions for each button and their associated functions
        actions = [
            ("Start", self.start),
            ("Stop", self.stop),
            ("Step", self.step),
            ("Clear", self.clear),
            ("Random", self.randomize),
            ("Save", self.controller.save_grid),
            ("Load", self.controller.load_grid),
            ("Glider", self.insert_glider),
            ("Theme", self.toggle_theme)
        ]

        # Create and pack buttons
        for (text, cmd) in actions:
            b = tk.Button(button_frame, text=text, command=cmd, width=10)
            b.pack(side=tk.LEFT, padx=2, pady=5)

        # Create a speed control slider to adjust the simulation speed
        self.speed_slider = tk.Scale(self.root, from_=50, to=1000, orient=tk.HORIZONTAL, label="Speed (ms)", command=self.change_speed)
        self.speed_slider.set(self.controller.speed)  # Set the initial value of the speed slider
        self.speed_slider.pack(pady=5)

    def _on_canvas_click(self, event):
        # Handle a click event on the canvas (toggle the cell state)
        row, col = event.y // self.cell_size, event.x // self.cell_size
        self.grid.toggle_cell(row, col)  # Toggle the cell at the clicked position
        self._draw_grid()  # Redraw the grid after toggling

    def _draw_grid(self):
        # Clear the canvas and redraw the grid
        self.canvas.delete("all")
        bg = self.theme.get_color("background")  # Background color
        alive_color = self.theme.get_color("alive")  # Color for alive cells
        grid_color = self.theme.get_color("grid_line")  # Color for grid lines

        # Iterate over the grid and draw rectangles for each cell
        for i in range(self.grid.rows):
            for j in range(self.grid.cols):
                color = alive_color if self.grid.grid[i][j] else bg  # Determine cell color based on its state
                self.canvas.create_rectangle(
                    j * self.cell_size, i * self.cell_size,
                    (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                    fill=color, outline=grid_color  # Draw a rectangle with the appropriate color and grid outline
                )

    def _update(self):
        # If the simulation is running, update the grid with the next generation
        if self.controller.running:
            self.controller.step()  # Go to the next generation
            self._draw_grid()  # Redraw the grid
            self.root.after(self.controller.speed, self._update)  # Schedule the next update after the specified speed

    # Button functions to control the game
    def start(self):
        self.controller.start()  # Start the simulation
        self._update()  # Begin updating the grid

    def stop(self):
        self.controller.stop()  # Stop the simulation

    def step(self):
        self.controller.step()  # Step through one generation
        self._draw_grid()  # Redraw the grid after stepping

    def clear(self):
        self.controller.clear()  # Clear the grid
        self._draw_grid()  # Redraw the grid

    def randomize(self):
        self.controller.randomize()  # Randomize the grid
        self._draw_grid()  # Redraw the grid

    def insert_glider(self):
        self.controller.insert_glider()  # Insert a glider pattern
        self._draw_grid()  # Redraw the grid

    def toggle_theme(self):
        self.theme.toggle_theme()  # Toggle between dark and light theme
        self._draw_grid()  # Redraw the grid with the new theme

    def change_speed(self, val):
        # Change the speed of the simulation based on the slider value
        self.controller.speed = int(val)
