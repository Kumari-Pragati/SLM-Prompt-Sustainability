import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string("HelloWorld123"), ['Valid string.'])

    def test_empty_string(self):
        self.assertEqual(check_string(""), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_single_uppercase(self):
        self.assertEqual(check_string("Hello"), ['String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_single_lowercase(self):
        self.assertEqual(check_string("hello"), ['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_single_digit(self):
        self.assertEqual(check_string("hello123"), ['String must have 1 upper case character.', 'String length should be atleast 8.'])

    def test_valid_string_with_numbers(self):
        self.assertEqual(check_string("Hello123World"), ['Valid string.'])

    def test_valid_string_with_uppercase(self):
        self.assertEqual(check_string("HelloWorld123"), ['Valid string.'])

    def test_valid_string_with_lowercase(self):
        self.assertEqual(check_string("helloWorld123"), ['Valid string.'])

    def test_invalid_string(self):
        self.assertEqual(check_string("123"), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String length should be atleast 8.'])
