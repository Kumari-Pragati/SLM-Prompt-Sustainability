import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_str("Hello"), "Valid")

    def test_invalid_string(self):
        self.assertEqual(check_str("123"), "Invalid")

    def test_valid_string_with_uppercase(self):
        self.assertEqual(check_str("HelloWorld"), "Valid")

    def test_valid_string_with_special_characters(self):
        self.assertEqual(check_str("Hello_World"), "Valid")

    def test_invalid_string_with_numbers(self):
        self.assertEqual(check_str("Hello123"), "Invalid")

    def test_invalid_string_with_punctuation(self):
        self.assertEqual(check_str("Hello!"), "Invalid")

    def test_invalid_string_with_spaces(self):
        self.assertEqual(check_str("Hello World"), "Invalid")

    def test_invalid_string_with_empty_string(self):
        self.assertEqual(check_str(""), "Invalid")
