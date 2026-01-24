import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(check_String("abc123"))

    def test_empty_string(self):
        self.assertFalse(check_String(""))

    def test_all_alphabet(self):
        self.assertFalse(check_String("abcdefghijklmnopqrstuvwxyz"))

    def test_all_numbers(self):
        self.assertFalse(check_String("1234567890"))

    def test_single_alphabet_or_number(self):
        self.assertFalse(check_String("a"))
        self.assertFalse(check_String("1"))

    def test_mixed_case(self):
        self.assertTrue(check_String("AbC123"))

    def test_special_characters(self):
        self.assertFalse(check_String("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"))
