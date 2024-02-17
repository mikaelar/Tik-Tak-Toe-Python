import unittest
from unittest.mock import patch
from main import (
    TicTacToe,
)  # Make sure to replace 'your_module' with the name of the Python file containing your TicTacToe class


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
        self.game.symbols = ["X", "O"]  # Simplifying symbols for testing

    def test_toggle_bot(self):
        initial_state = self.game.play_with_bot
        self.game.toggle_bot()
        self.assertNotEqual(initial_state, self.game.play_with_bot)

    def test_check_winner(self):
        # Setting up a winning condition for horizontal, vertical, and diagonal wins
        for row in range(3):
            self.game.board_buttons[row] = [{"text": "X"}, {"text": "X"}, {"text": "X"}]
            self.assertTrue(self.game.check_winner())
            self.setUp()  # Reset game state for the next scenario

        for col in range(3):
            self.game.board_buttons[0][col]["text"] = "X"
            self.game.board_buttons[1][col]["text"] = "X"
            self.game.board_buttons[2][col]["text"] = "X"
            self.assertTrue(self.game.check_winner())
            self.setUp()  # Reset game state for the next scenario

        self.game.board_buttons = [
            [{"text": "X" if i == j else ""} for j in range(3)] for i in range(3)
        ]
        self.assertTrue(self.game.check_winner())
        self.setUp()  # Reset game state for the next scenario

        self.game.board_buttons = [
            [{"text": "X" if i + j == 2 else ""} for j in range(3)] for i in range(3)
        ]
        self.assertTrue(self.game.check_winner())

    def test_is_board_full(self):
        self.assertFalse(self.game.is_board_full())
        for row in range(3):
            for col in range(3):
                self.game.board_buttons[row][col] = {"text": "X"}
        self.assertTrue(self.game.is_board_full())

    @patch("random.choice")
    def test_bot_make_move(self, mock_choice):
        mock_choice.return_value = (0, 0)
        self.game.board_buttons = [[{"text": ""} for _ in range(3)] for _ in range(3)]
        self.game.symbols = ["X", "O"]
        self.game.current_player = "Player 2"
        self.game.symbol_option_var.set(
            1
        )  # Assuming this sets up the symbols correctly
        self.game.bot_make_move()
        # Check if a move was made
        self.assertNotEqual(self.game.board_buttons[0][0]["text"], "")


if __name__ == "__main__":
    unittest.main()
