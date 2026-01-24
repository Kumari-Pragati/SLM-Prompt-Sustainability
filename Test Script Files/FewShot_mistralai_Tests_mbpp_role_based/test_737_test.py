import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_str("A1b2"), "Valid")
        self.assertEqual(check_str("a1B2_3"), "Valid")
        self.assertEqual(check_str("IoU_123"), "Valid")

    def test_invalid_string_no_first_vowel(self):
        self.assertEqual(check_str("123"), "Invalid")
        self.assertEqual(check_str("_123"), "Invalid")
        self.assertEqual(check_str("123_"), "Invalid")

    def test_invalid_string_no_alphanumeric_characters(self):
        self.assertEqual(check_str("A"), "Invalid")
        self.assertEqual(check_str("IoU"), "Invalid")
        self.assertEqual(check_str("_"), "Invalid")

    def test_invalid_string_special_characters(self):
        self.assertEqual(check_str("A!1b2"), "Invalid")
        self.assertEqual(check_str("a1B2_#"), "Invalid")
        self.assertEqual(check_str("IoU_123@"), "Invalid")
