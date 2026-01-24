import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_single_lowercase_letter(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_multiple_lowercase_letters(self):
        self.assertEqual(check_char("abc"), "Invalid")
        self.assertEqual(check_char("xyz"), "Invalid")

    def test_mixed_case_letters(self):
        self.assertEqual(check_char("Abc"), "Invalid")
        self.assertEqual(check_char("123abc"), "Invalid")
        self.assertEqual(check_char("abc123"), "Invalid")

    def test_special_characters(self):
        self.assertEqual(check_char("a#"), "Invalid")
        self.assertEqual(check_char("@abc"), "Invalid")
        self.assertEqual(check_char("abc@"), "Invalid")

    def test_numbers(self):
        self.assertEqual(check_char("123"), "Invalid")
        self.assertEqual(check_char("1a"), "Invalid")
        self.assertEqual(check_char("a1"), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_whitespace(self):
        self.assertEqual(check_char(" "), "Invalid")
        self.assertEqual(check_char("\t"), "Invalid")
        self.assertEqual(check_char("\n"), "Invalid")
