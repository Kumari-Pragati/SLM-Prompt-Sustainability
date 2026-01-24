import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_single_lowercase_letter(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_string_with_same_first_and_last_letter(self):
        self.assertEqual(check_char('aabbaa'), "Valid")

    def test_string_with_different_first_and_last_letter(self):
        self.assertEqual(check_char('abcabc'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_string_with_uppercase_letter(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_string_with_special_characters(self):
        self.assertEqual(check_char('a$b'), "Invalid")
