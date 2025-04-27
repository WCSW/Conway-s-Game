class ThemeManager:
    # Define the available themes as a dictionary
    THEMES = {
        "dark": {  # Dark theme settings
            "background": "#1e1e1e",  # Dark background color
            "grid_line": "#444",  # Grid line color for dark theme
            "alive": "#00ff00",  # Alive cell color (green)
            "text": "white"  # Text color (white)
        },
        "light": {  # Light theme settings
            "background": "#ffffff",  # Light background color
            "grid_line": "#ccc",  # Grid line color for light theme
            "alive": "#000000",  # Alive cell color (black)
            "text": "black"  # Text color (black)
        }
    }

    def __init__(self):
        # Initialize the theme manager with the default theme set to "dark"
        self.current_theme = "dark"

    def toggle_theme(self):
        # Toggle between light and dark themes
        self.current_theme = "light" if self.current_theme == "dark" else "dark"

    def get_color(self, element):
        # Return the color for the specified element (background, grid_line, alive, text) based on the current theme
        return self.THEMES[self.current_theme][element]
