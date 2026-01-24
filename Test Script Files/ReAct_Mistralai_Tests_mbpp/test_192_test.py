import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_String(""))

    def test_all_alphabet(self):
        self.assertTrue(check_String("abcdefghijklmnopqrstuvwxyz"))

    def test_all_numbers(self):
        self.assertTrue(check_String("1234567890"))

    def test_mixed_alphabet_numbers(self):
        self.assertTrue(check_String("abc123def456"))

    def test_single_alphabet_and_number(self):
        self.assertTrue(check_String("a1"))
        self.assertTrue(check_String("1a"))

    def test_leading_alphabet_trailing_number(self):
        self.assertTrue(check_String("a1"))
        self.assertTrue(check_String("1a"))

    def test_leading_number_trailing_alphabet(self):
        self.assertTrue(check_String("1a"))
        self.assertTrue(check_String("a1"))

    def test_all_uppercase(self):
        self.assertTrue(check_String("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_all_uppercase_numbers(self):
        self.assertTrue(check_String("1234567890"))

    def test_mixed_uppercase_numbers(self):
        self.assertTrue(check_String("ABC123DEF456"))

    def test_single_uppercase_and_number(self):
        self.assertTrue(check_String("A1"))
        self.assertTrue(check_String("1A"))

    def test_leading_uppercase_trailing_number(self):
        self.assertTrue(check_String("A1"))
        self.assertTrue(check_String("1A"))

    def test_leading_number_trailing_uppercase(self):
        self.assertTrue(check_String("1A"))
        self.assertTrue(check_String("A1"))

    def test_special_characters(self):
        self.assertFalse(check_String("!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))

    def test_empty_list(self):
        self.assertFalse(check_String(""))

    def test_single_character(self):
        for char in "!@#$%^&*()_+-=[]{}|;:'\",.<>/?abcdefghijklmnopqrstuvwxyz0123456789":
            self.assertFalse(check_String(char))
