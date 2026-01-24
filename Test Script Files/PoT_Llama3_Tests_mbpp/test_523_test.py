import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_string("Hello123World"), ['Valid string.'])

    def test_uppercase(self):
        self.assertEqual(check_string("hello123world"), ['String must have 1 upper case character.'])

    def test_lowercase(self):
        self.assertEqual(check_string("HELLO123WORLD"), ['String must have 1 lower case character.'])

    def test_digit(self):
        self.assertEqual(check_string("HelloWorld"), ['String must have 1 number.'])

    def test_length(self):
        self.assertEqual(check_string("HelloWorld123"), ['String length should be atleast 8.'])

    def test_all_conditions(self):
        self.assertEqual(check_string("HELLO123WORLD"), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_valid_string(self):
        self.assertEqual(check_string("HelloWorld123"), ['Valid string.'])

    def test_empty_string(self):
        self.assertEqual(check_string(""), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_single_character(self):
        self.assertEqual(check_string("a"), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])
