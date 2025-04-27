import tkinter as tk  # Import the tkinter module for GUI functionality
from grid import Grid  # Import the Grid class for representing the game grid
from controller import GameController  # Import the GameController class to manage the game logic
from ui import GameUI  # Import the GameUI class to handle the user interface
from theme_manager import ThemeManager  # Import the ThemeManager class to manage the application's theme

# The main function that sets up and runs the application
def main():
    root = tk.Tk()  # Create the root window for the application
    root.title("Conway's Game of Life - Super Pro Multi-Class")  # Set the window title

    # Create an instance of the Grid class with 30 rows and 30 columns
    grid = Grid(rows=30, cols=30)
    # Create an instance of the GameController class, passing the grid object
    controller = GameController(grid)
    # Create an instance of the ThemeManager class to manage the application's theme
    theme_manager = ThemeManager()
    # Create an instance of the GameUI class, passing the root window, grid, controller, and theme manager
    ui = GameUI(root, grid, controller, theme_manager)

    # Start the Tkinter main loop to run the application
    root.mainloop()

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the application
