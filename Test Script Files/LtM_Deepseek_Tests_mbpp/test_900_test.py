import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(match_num("5"))

    def test_simple_invalid_input(self):
        self.assertFalse(match_num("4"))

    def test_empty_input(self):
        self.assertFalse(match_num(""))

    def test_input_with_leading_characters(self):
        self.assertFalse(match_num("a5"))

    def test_input_with_trailing_characters(self):
        self.assertFalse(match_num("5a"))

    def test_input_with_multiple_characters(self):
        self.assertFalse(match_num("5a5"))

    def test_input_with_number_at_start(self):
        self.assertFalse(match_num("15"))

    def test_input_with_number_at_end(self):
        self.assertFalse(match_num("51"))
