import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(dig_let("hello123"), (4, 3))

    def test_edge_case_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_edge_case_single_digit(self):
        self.assertEqual(dig_let("1"), (0, 1))

    def test_edge_case_single_alpha(self):
        self.assertEqual(dig_let("a"), (1, 0))

    def test_edge_case_mixed_input(self):
        self.assertEqual(dig_let("abc123"), (3, 3))

    def test_edge_case_all_digits(self):
        self.assertEqual(dig_let("123456"), (0, 6))

    def test_edge_case_all_alpha(self):
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))

    def test_edge_case_mixed_input_with_spaces(self):
        self.assertEqual(dig_let("abc 123"), (3, 3))

    def test_edge_case_mixed_input_with_punctuation(self):
        self.assertEqual(dig_let("abc!123"), (3, 3))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            dig_let(123)
