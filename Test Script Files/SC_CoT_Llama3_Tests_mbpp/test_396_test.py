import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_single_char(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_valid_multiple_chars(self):
        self.assertEqual(check_char('abc'), "Invalid")

    def test_valid_repeated_chars(self):
        self.assertEqual(check_char('aa'), "Valid")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_char(123)

    def test_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_single_digit(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_single_uppercase(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_single_non_alphabet(self):
        self.assertEqual(check_char('!'), "Invalid")

    def test_valid_string(self):
        self.assertEqual(check_char('hello'), "Invalid")

    def test_valid_string_with_spaces(self):
        self.assertEqual(check_char('hello world'), "Invalid")

    def test_valid_string_with_punctuation(self):
        self.assertEqual(check_char('hello!'), "Invalid")

    def test_valid_string_with_numbers(self):
        self.assertEqual(check_char('hello123'), "Invalid")
