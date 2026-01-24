import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string("ValidString"), ['Valid string.'])

    def test_string_with_only_upper_case(self):
        self.assertEqual(check_string("UPPERCASESTRING"), ['String must have 1 lower case character.'])

    def test_string_with_only_lower_case(self):
        self.assertEqual(check_string("lowercasestring"), ['String must have 1 upper case character.'])

    def test_string_with_only_numbers(self):
        self.assertEqual(check_string("12345678"), ['String must have 1 lower case character.', 'String must have 1 upper case character.'])

    def test_string_with_only_special_characters(self):
        self.assertEqual(check_string("!@#$%^&*()_+-="), ['String must have 1 lower case character.', 'String must have 1 upper case character.', 'String must have 1 number.'])

    def test_string_with_minimal_length(self):
        self.assertEqual(check_string("abcdefg"), ['String length should be atleast 8.'])
