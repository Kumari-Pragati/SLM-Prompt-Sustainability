import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_string('HelloWorld123'), ['Valid string.'])

    def test_string_with_uppercase(self):
        self.assertEqual(check_string('helloWorld123'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'Valid string.'])

    def test_string_with_lowercase(self):
        self.assertEqual(check_string('HELLO123'), ['String must have 1 upper case character.', 'String must have 1 number.', 'Valid string.'])

    def test_string_with_digits(self):
        self.assertEqual(check_string('Hello123'), ['String must have 1 lower case character.', 'String must have 1 number.', 'Valid string.'])

    def test_string_with_length(self):
        self.assertEqual(check_string('Hello123456'), ['Valid string.'])

    def test_string_with_invalid_length(self):
        self.assertEqual(check_string('Hello'), ['String length should be atleast 8.'])

    def test_empty_string(self):
        self.assertEqual(check_string(''), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_string_with_no_characters(self):
        self.assertEqual(check_string(''), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])
