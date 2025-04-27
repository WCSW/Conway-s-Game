class ThemeManager:
    THEMES = {
        "dark": {
            "background": "#1e1e1e",
            "grid_line": "#444",
            "alive": "#00ff00",
            "text": "white"
        },
        "light": {
            "background": "#ffffff",
            "grid_line": "#ccc",
            "alive": "#000000",
            "text": "black"
        }
    }

    def __init__(self):
        self.current_theme = "dark"

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"

    def get_color(self, element):
        return self.THEMES[self.current_theme][element]
