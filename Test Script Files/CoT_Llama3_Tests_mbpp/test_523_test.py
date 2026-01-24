import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string('Hello123'), ['Valid string.'])

    def test_string_with_uppercase(self):
        self.assertEqual(check_string('HELLO123'), ['String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_lowercase(self):
        self.assertEqual(check_string('hello123'), ['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_digits(self):
        self.assertEqual(check_string('Hello12345'), ['String must have 1 lower case character.', 'String length should be atleast 8.'])

    def test_string_with_upper_and_lowercase(self):
        self.assertEqual(check_string('Hellohello123'), ['String length should be atleast 8.'])

    def test_string_with_digits_and_uppercase(self):
        self.assertEqual(check_string('Hello12345'), ['String must have 1 lower case character.', 'String length should be atleast 8.'])

    def test_string_with_digits_and_lowercase(self):
        self.assertEqual(check_string('hello12345'), ['String must have 1 upper case character.', 'String length should be atleast 8.'])

    def test_string_with_all_conditions(self):
        self.assertEqual(check_string('Hello1234567'), [])

    def test_empty_string(self):
        self.assertEqual(check_string(''), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_single_character(self):
        self.assertEqual(check_string('a'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])
