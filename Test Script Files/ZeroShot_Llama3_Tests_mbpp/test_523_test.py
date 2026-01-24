import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_string("HelloWorld123"), ['Valid string.'])

    def test_invalid_string(self):
        self.assertEqual(check_string("hello"), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])
        self.assertEqual(check_string("HELLO"), ['String must have 1 lower case character.'])
        self.assertEqual(check_string("1234567"), ['String length should be atleast 8.'])
        self.assertEqual(check_string("Hello"), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])
        self.assertEqual(check_string("123"), ['String must have 1 number.'])
        self.assertEqual(check_string("abcdef"), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])
        self.assertEqual(check_string("1234567"), ['String length should be atleast 8.'])

    def test_multiple_conditions(self):
        self.assertEqual(check_string("Hello123"), ['String must have 1 lower case character.'])
        self.assertEqual(check_string("HELLO123"), ['String must have 1 lower case character.'])
        self.assertEqual(check_string("hello123"), ['String must have 1 upper case character.'])
        self.assertEqual(check_string("12345678"), ['Valid string.'])
