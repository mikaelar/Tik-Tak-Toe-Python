import sys
import random
import tkinter as tk
from tkinter import messagebox
from guiutils import GUIUtils
from stats_manager import write_stat, read_stats


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe for Kids")

        self.symbols_options = {1: ["🌊", "🦈"], 2: ["🦀", "🐋"], 3: ["🐚", "🦐"]}

        self.players = ["Player 1", "Player 2"]
        self.current_player = random.choice(self.players)
        self.play_with_bot = False
        self.symbols = None
        self.board_buttons = [[None, None, None] for _ in range(3)]

        self.symbol_option_var = tk.IntVar()
        self.symbol_option_var.set(1)

        self.player_size = tk.IntVar()
        self.player_size.set(24)

        self.num_games_var = tk.IntVar()
        self.num_games_var.set(1)

        self.games_played = 0

        self.current_player_label = tk.Label()

    def toggle_bot(self):
        self.play_with_bot = not self.play_with_bot

    def check_winner(self):
        for i in range(3):
            if (
                self.board_buttons[i][0]["text"]
                == self.board_buttons[i][1]["text"]
                == self.board_buttons[i][2]["text"]
                != ""
            ):
                write_stat(
                    winner=f"{self.current_player}", player_symbols=f"{self.symbols}"
                )
                return True
            if (
                self.board_buttons[0][i]["text"]
                == self.board_buttons[1][i]["text"]
                == self.board_buttons[2][i]["text"]
                != ""
            ):
                write_stat(
                    winner=f"{self.current_player}", player_symbols=f"{self.symbols}"
                )
                return True
        if (
            self.board_buttons[0][0]["text"]
            == self.board_buttons[1][1]["text"]
            == self.board_buttons[2][2]["text"]
            != ""
            or self.board_buttons[0][2]["text"]
            == self.board_buttons[1][1]["text"]
            == self.board_buttons[2][0]["text"]
            != ""
        ):
            write_stat(
                winner=f"{self.current_player}", player_symbols=f"{self.symbols}"
            )
            return True
        return False

    def is_board_full(self):
        for row in self.board_buttons:
            for button in row:
                if button["text"] == "":
                    return False
        write_stat(winner=f"{self.current_player}", player_symbols=f"{self.symbols}")
        return True

    def on_click(self, row, col):
        if self.board_buttons[row][col]["text"] == "":
            self.board_buttons[row][col]["text"] = self.symbols[
                self.players.index(self.current_player)
            ]
            if self.check_winner():
                if self.play_with_bot:
                    messagebox.showinfo("Game Over", "Great play with the bot!")
                else:
                    messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.games_played += 1
                if self.games_played < self.num_games_var.get():
                    messagebox.showinfo(
                        "Remaining games",
                        f"Remainng {self.num_games_var.get()-self.games_played} games!",
                    )
                    self.reset_game()
                else:
                    self.root.destroy()
                    sys.exit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.games_played += 1
                if self.games_played < self.num_games_var.get():
                    messagebox.showinfo(
                        "Remaining games",
                        f"Remainng {self.num_games_var.get()-self.games_played} games!",
                    )
                    self.reset_game()
                else:
                    self.root.destroy()
                    sys.exit()
            else:
                if not self.play_with_bot:
                    self.current_player = (
                        self.players[1]
                        if self.current_player == self.players[0]
                        else self.players[0]
                    )
                else:
                    self.bot_make_move()
                self.update_current_player_label()

    def bot_make_move(self):
        empty_cells = [
            (i, j)
            for i in range(3)
            for j in range(3)
            if self.board_buttons[i][j]["text"] == ""
        ]
        if empty_cells:
            row, col = random.choice(empty_cells)
            bot_symbol_index = (
                1
                if self.symbols_options[self.symbol_option_var.get()][0]
                == self.symbols_options[self.symbol_option_var.get()][
                    self.players.index(self.current_player)
                ]
                else 0
            )
            bot_symbol = self.symbols_options[self.symbol_option_var.get()][
                bot_symbol_index
            ]
            self.board_buttons[row][col]["text"] = bot_symbol
            self.current_player_label_bot = tk.Label(
                self.root, text=f"Current Player: {self.current_player}"
            )
            self.current_player_label_bot.grid(row=1, column=3, rowspan=3, padx=10)
            print(f"{self.current_player}")

    def set_options(self):
        self.symbols = self.symbols_options[self.symbol_option_var.get()]
        self.root.withdraw()

        option_window = tk.Toplevel(self.root)
        option_window.title("Tic-Tac-Toe Game")

        label = tk.Label(
            option_window,
            text="Welcome! Here you can set up your game:",
            font=("Helvetica", 16),
        )
        label.pack(padx=15, pady=10)

        subheading_font = ("Arial", 15, "bold")

        label_size = tk.Label(
            option_window, text="Symbol Option:", font=subheading_font, fg="#FFA07A"
        )
        label_size.pack(pady=(5, 10))

        GUIUtils.visualize_symbols(option_window)

        symbol_option_menu = tk.OptionMenu(
            option_window, self.symbol_option_var, *self.symbols_options.keys()
        )
        symbol_option_menu.pack(pady=10)

        label_size = tk.Label(
            option_window, text="Game Board Size:", font=subheading_font, fg="#87CEEB"
        )
        label_size.pack(pady=(5, 10))

        size_option_menu = tk.OptionMenu(option_window, self.player_size, 16, 24, 32)
        size_option_menu.pack(pady=10)

        label_num_games = tk.Label(
            option_window, text="Number of Games:", font=subheading_font, fg="#FFA07A"
        )
        label_num_games.pack(pady=(5, 10))

        num_games_entry = tk.Entry(
            option_window, textvariable=self.num_games_var, width=5
        )
        num_games_entry.pack(pady=10)

        play_with_bot_message = tk.Label(
            option_window,
            text="Do you want to play with bot?",
            font=subheading_font,
            fg="#87CEEB",
        )
        play_with_bot_message.pack(pady=10)
        play_with_bot_checkbox_yes = tk.Checkbutton(
            option_window,
            text="Yes 🤖",
            variable=tk.BooleanVar(),
            command=self.toggle_bot,
        )
        play_with_bot_checkbox_yes.pack(pady=10)

        button_start_game = tk.Button(
            option_window,
            text="Start Game",
            command=lambda: self.start_game(option_window),
        )
        button_start_game.pack(pady=10)

        GUIUtils.center_window(option_window)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board_buttons[i][j]["text"] = ""
        self.update_current_player_label()

    def start_game(self, option_window):
        option_window.destroy()
        self.symbols = self.symbols_options[self.symbol_option_var.get()]

        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe for Kids")

        self.current_player = random.choice(self.players)
        self.update_current_player_label()

        for i in range(3):
            for j in range(3):
                self.board_buttons[i][j] = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", self.player_size.get()),
                    width=3,
                    height=3,
                    command=lambda i=i, j=j: self.on_click(i, j),
                )
                self.board_buttons[i][j].grid(row=i + 1, column=j)
                if not self.play_with_bot:
                    self.current_player_label = tk.Label(
                        self.root, text=f"Current Player: {self.current_player}"
                    )
                    self.current_player_label.grid(row=1, column=3, rowspan=3, padx=10)
                else:
                    self.current_player_label = tk.Label(
                        self.root, text=f"You are playing with bot. It's your turn!"
                    )
                    self.current_player_label.grid(row=1, column=3, rowspan=3, padx=10)

        GUIUtils.center_window(self.root)

        self.root.mainloop()

    def update_current_player_label(self):
        if not self.play_with_bot:
            self.current_player_label.config(
                text=f"Current Player: {self.current_player}"
            )
        else:
            self.current_player_label = tk.Label(
                self.root, text=f"You are playing with bot. It's your turn!"
            )
            self.current_player_label.grid(row=1, column=3, rowspan=3, padx=10)


if __name__ == "__main__":
    game = TicTacToe()
    game.set_options()
    game.root.mainloop()
    print("Game Statistics:")
    read_stats()
