import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_all_digits(self):
        self.assertEqual(dig_let("1234567890"), (0, 10))

    def test_all_letters(self):
        self.assertEqual(dig_let("abcdefghijklmnopqrstuvwxyz"), (26, 0))

    def test_mixed_digits_and_letters(self):
        self.assertEqual(dig_let("abc123def456"), (9, 6))

    def test_digits_and_letters_and_punctuation(self):
        self.assertEqual(dig_let("abc123!@#$def456"), (9, 6))

    def test_all_punctuation(self):
        self.assertEqual(dig_let("!!!!!!!"), (0, 0))

    def test_non_ascii_characters(self):
        self.assertEqual(dig_let("abc123!@#$€def456"), (9, 6))
