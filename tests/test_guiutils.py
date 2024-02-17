import unittest
from unittest.mock import MagicMock
from guiutils import GUIUtils


class TestGUIUtils(unittest.TestCase):

    def test_center_window(self):
        mock_window = MagicMock()
        mock_window.winfo_screenwidth.return_value = 800
        mock_window.winfo_screenheight.return_value = 600
        mock_window.winfo_reqwidth.return_value = 400
        mock_window.winfo_reqheight.return_value = 300

        expected_geometry = "+200+150"

        GUIUtils.center_window(mock_window)

        mock_window.geometry.assert_called_once_with(expected_geometry)
