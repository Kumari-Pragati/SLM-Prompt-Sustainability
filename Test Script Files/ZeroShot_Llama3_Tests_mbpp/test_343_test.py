import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_string_with_digits(self):
        self.assertEqual(dig_let("123"), (0, 3))

    def test_string_with_letters(self):
        self.assertEqual(dig_let("abc"), (3, 0))

    def test_string_with_digits_and_letters(self):
        self.assertEqual(dig_let("abc123"), (3, 3))

    def test_string_with_punctuation(self):
        self.assertEqual(dig_let("abc!@#"), (3, 0))

    def test_string_with_spaces(self):
        self.assertEqual(dig_let("abc   "), (3, 0))

    def test_string_with_newline(self):
        self.assertEqual(dig_let("abc\n"), (3, 0))

    def test_string_with_tabs(self):
        self.assertEqual(dig_let("abc\t"), (3, 0))
