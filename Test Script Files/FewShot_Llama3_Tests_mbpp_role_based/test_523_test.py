import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string('Hello123'), ['Valid string.'])

    def test_string_with_uppercase(self):
        self.assertEqual(check_string('HELLO123'), ['String must have 1 lower case character.', 'String must have 1 number.', 'Valid string.'])

    def test_string_with_lowercase(self):
        self.assertEqual(check_string('hello123'), ['String must have 1 upper case character.', 'String must have 1 number.', 'Valid string.'])

    def test_string_with_digits(self):
        self.assertEqual(check_string('Hello456'), ['String must have 1 lower case character.', 'String must have 1 upper case character.', 'Valid string.'])

    def test_string_with_length_less_than_7(self):
        self.assertEqual(check_string('Hello'), ['String length should be atleast 8.'])

    def test_string_with_length_7(self):
        self.assertEqual(check_string('Hello1234'), ['Valid string.'])

    def test_string_with_length_greater_than_7(self):
        self.assertEqual(check_string('Hello123456'), ['Valid string.'])
