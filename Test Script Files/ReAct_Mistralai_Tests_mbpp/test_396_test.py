import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_single_lowercase_letter(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("z"), "Valid")

    def test_valid_multi_lowercase_letters(self):
        self.assertEqual(check_char("abc"), "Invalid")
        self.assertEqual(check_char("xyz"), "Invalid")

    def test_valid_single_lowercase_letter_with_trailing_spaces(self):
        self.assertEqual(check_char("a "), "Invalid")
        self.assertEqual(check_char("z "), "Invalid")

    def test_valid_multi_lowercase_letters_with_trailing_spaces(self):
        self.assertEqual(check_char("abc "), "Invalid")
        self.assertEqual(check_char("xyz "), "Invalid")

    def test_valid_single_lowercase_letter_with_leading_spaces(self):
        self.assertEqual(check_char(" a"), "Invalid")
        self.assertEqual(check_char(" z"), "Invalid")

    def test_valid_multi_lowercase_letters_with_leading_spaces(self):
        self.assertEqual(check_char(" abc"), "Invalid")
        self.assertEqual(check_char(" xyz"), "Invalid")

    def test_valid_single_lowercase_letter_with_leading_and_trailing_spaces(self):
        self.assertEqual(check_char(" a "), "Invalid")
        self.assertEqual(check_char(" z "), "Invalid")

    def test_valid_multi_lowercase_letters_with_leading_and_trailing_spaces(self):
        self.assertEqual(check_char(" a bc "), "Invalid")
        self.assertEqual(check_char(" x y z "), "Invalid")

    def test_invalid_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_invalid_string_with_digits(self):
        self.assertEqual(check_char("a1"), "Invalid")
        self.assertEqual(check_char("z9"), "Invalid")

    def test_invalid_string_with_special_characters(self):
        self.assertEqual(check_char("a#"), "Invalid")
        self.assertEqual(check_char("z@"), "Invalid")

    def test_invalid_string_with_uppercase_letters(self):
        self.assertEqual(check_char("A"), "Invalid")
        self.assertEqual(check_char("Z"), "Invalid")

    def test_invalid_string_with_multiple_uppercase_letters(self):
        self.assertEqual(check_char("AB"), "Invalid")
        self.assertEqual(check_char("XY"), "Invalid")
