import tkinter as tk


class GUIUtils:
    def center_window(window):
        """Centers a tkinter window on the screen."""
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = window.winfo_reqwidth()
        window_height = window.winfo_reqheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        window.geometry(f"+{x}+{y}")

    def visualize_symbols(window):
        """Visualizes symbols in the option window."""
        tk.Label(window, text="1: 🌊 🦈").pack(pady=(5, 0))

        tk.Label(window, text="2: 🦀 🐋").pack(pady=(5, 0))

        tk.Label(window, text="3: 🐚 🦐").pack(pady=(5, 10))
