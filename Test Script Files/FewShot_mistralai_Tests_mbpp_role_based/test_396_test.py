import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_valid_single_lowercase_letter(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_valid_multi_lowercase_letters(self):
        self.assertEqual(check_char("hello"), "Invalid")
        self.assertEqual(check_char("ZZZ"), "Invalid")

    def test_valid_multi_lowercase_letters_with_repeated_char(self):
        self.assertEqual(check_char("aaa"), "Valid")
        self.assertEqual(check_char("zzz"), "Valid")

    def test_invalid_uppercase_letter(self):
        self.assertEqual(check_char("A"), "Invalid")

    def test_invalid_special_characters(self):
        self.assertEqual(check_char("!@#$%^&*()"), "Invalid")

    def test_invalid_number(self):
        self.assertEqual(check_char("123"), "Invalid")

    def test_invalid_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")
