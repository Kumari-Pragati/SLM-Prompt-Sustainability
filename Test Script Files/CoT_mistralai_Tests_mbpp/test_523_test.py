import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_string('ValidString'), ['Valid string.'])

    def test_string_with_upper_case_and_lower_case(self):
        self.assertEqual(check_string('AbCd1234'), ['Valid string.'])

    def test_string_with_upper_case_and_number(self):
        self.assertEqual(check_string('AbC123'), ['Valid string.'])

    def test_string_with_lower_case_and_number(self):
        self.assertEqual(check_string('aBc123'), ['Valid string.'])

    def test_string_with_upper_case_lower_case_and_number(self):
        self.assertEqual(check_string('AbCd123'), ['Valid string.'])

    def test_string_with_minimum_length(self):
        self.assertEqual(check_string('AbCd12345'), ['Valid string.'])

    def test_string_with_only_upper_case(self):
        self.assertEqual(check_string('ABCDEFG'), ['String must have 1 lower case character.', 'String length should be atleast 8.'])

    def test_string_with_only_lower_case(self):
        self.assertEqual(check_string('abcdefg'), ['String must have 1 upper case character.', 'String length should be atleast 8.'])

    def test_string_with_only_number(self):
        self.assertEqual(check_string('1234567'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String length should be atleast 8.'])

    def test_string_with_empty_space(self):
        self.assertEqual(check_string(' '), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_only_special_characters(self):
        self.assertEqual(check_string('!@#$%^&*()'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_special_characters_and_alphanumeric(self):
        self.assertEqual(check_string('AbC!@#$%^&*()123'), ['Valid string.'])
