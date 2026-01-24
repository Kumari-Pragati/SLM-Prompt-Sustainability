import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(dig_let("Hello123"), (4, 3))

    def test_edge_case_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_edge_case_single_digit(self):
        self.assertEqual(dig_let("1"), (0, 1))

    def test_edge_case_single_letter(self):
        self.assertEqual(dig_let("a"), (1, 0))

    def test_edge_case_mixed_string(self):
        self.assertEqual(dig_let("Hello123abc"), (6, 6))

    def test_edge_case_no_digits_or_letters(self):
        self.assertEqual(dig_let("!*@#$"), (0, 0))

    def test_edge_case_no_letters(self):
        self.assertEqual(dig_let("1234567890"), (0, 10))

    def test_edge_case_no_digits(self):
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))
