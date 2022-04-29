from sys import argv
import unittest
from unittest import mock

from Guessing_game import guess, get_range, check_arg


class TestMain(unittest.TestCase):

   # @mock.patch("builtins.input", return_value=1)
   # def test_guess(self, mock_patch_output):
   #     answer = guess(1, 2)
   #     self.assertEqual(answer, 1)
   #
    @mock.patch("builtins.input", side_effect=["1", "2"])
    def test_get_range(self, mock_patch_output):
        getRange = get_range()
        self.assertEqual(getRange, (1, 2))

    @mock.patch("sys.argv", ["test_argv.py", "9", "2"])
    def test_check_arg(self):
        checkarg = check_arg()
        self.assertEqual(checkarg, (2, 9))
