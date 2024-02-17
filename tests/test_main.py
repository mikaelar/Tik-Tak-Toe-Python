import sys
import unittest
from unittest.mock import patch, MagicMock
from main import *


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
        self.game.board_buttons = [[{"text": ""} for _ in range(3)] for _ in range(3)]

    @patch("main.random.choice")
    def test_toggle_bot(self, mock_choice):
        initial_state = self.game.play_with_bot
        self.game.toggle_bot()
        self.assertNotEqual(initial_state, self.game.play_with_bot)

    def test_check_winner_horizontal(self):
        for i in range(3):
            self.game.board_buttons[0][i]["text"] = "X"
        self.assertTrue(self.game.check_winner())

    def test_check_winner_vertical(self):
        for i in range(3):
            self.game.board_buttons[i][0]["text"] = "X"
        self.assertTrue(self.game.check_winner())

    def test_check_winner_diagonal(self):
        for i in range(3):
            self.game.board_buttons[i][i]["text"] = "X"
        self.assertTrue(self.game.check_winner())

    def test_check_winner_no_win(self):
        self.game.board_buttons[0][0]["text"] = "X"
        self.game.board_buttons[1][1]["text"] = "O"
        self.assertFalse(self.game.check_winner())

    def test_is_board_full_true(self):
        for row in self.game.board_buttons:
            for cell in row:
                cell["text"] = "X"
        self.assertTrue(self.game.is_board_full())

    def test_is_board_full_false(self):
        self.game.board_buttons[0][0]["text"] = "X"
        self.assertFalse(self.game.is_board_full())

    @patch("main.sys.exit")
    @patch("tkinter.messagebox.showinfo")
    def test_on_click_win_condition(self, mock_showinfo, mock_sys_exit):
        self.game.symbols = ["X", "O"]
        self.game.current_player = "Player 1"
        self.game.board_buttons[0][0]["text"] = "X"
        self.game.board_buttons[0][1]["text"] = "X"
        self.game.on_click(0, 2)
        mock_showinfo.assert_called_with("Game Over", "Player 1 wins!")

        mock_sys_exit.assert_called_once()

    def test_reset_game_clears_board(self):
        self.game.board_buttons[0][0]["text"] = "X"
        self.game.board_buttons[1][1]["text"] = "O"
        self.game.board_buttons[2][2]["text"] = "X"

        self.game.reset_game()

        for row in self.game.board_buttons:
            for cell in row:
                self.assertEqual(cell["text"], "")

    @patch("random.choice")
    def test_bot_make_move_selects_symbol(self, mock_choice):
        mock_choice.return_value = (0, 1)

        self.game.symbol_option_var.set(1)
        self.game.current_player = "Player 2"

        self.game.bot_make_move()

        self.assertEqual(self.game.board_buttons[0][1]["text"], "🌊")

    @patch("tkinter.Toplevel")
    @patch("tkinter.OptionMenu")
    def test_symbols_option_updates_symbols(self, mock_option_menu, mock_toplevel):
        # Mock the selection of a symbol option
        self.game.symbol_option_var.set(
            2
        )  # Assuming this corresponds to the second set of symbols

        # Simulate the invocation of the method that would normally be triggered by GUI interaction
        self.game.set_options()

        # Verify that the symbols attribute is updated correctly
        expected_symbols = self.game.symbols_options[2]
        self.assertEqual(self.game.symbols, expected_symbols)

    def test_update_current_player_label(self):
        # Case 1: Update label for human players
        self.game.current_player = "Player 1"
        self.game.play_with_bot = False
        self.game.update_current_player_label()
        expected_label_text = "Current Player: Player 1"
        self.assertEqual(
            self.game.current_player_label.cget("text"),
            expected_label_text,
            "Label text incorrect for human player.",
        )

        # Case 2: Update label for playing with the bot
        self.game.play_with_bot = True
        self.game.update_current_player_label()
        expected_label_text_bot = "You are playing with bot. It's your turn!"
        self.assertEqual(
            self.game.current_player_label.cget("text"),
            expected_label_text_bot,
            "Label text incorrect for bot mode.",
        )


if __name__ == "__main__":
    unittest.main()
