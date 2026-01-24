import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(check_string('Abc12345'), ['Valid string.'])

    def test_no_uppercase(self):
        self.assertEqual(check_string('abc12345'), ['String must have 1 upper case character.'])

    def test_no_lowercase(self):
        self.assertEqual(check_string('ABC12345'), ['String must have 1 lower case character.'])

    def test_no_digit(self):
        self.assertEqual(check_string('AbcABC'), ['String must have 1 number.'])

    def test_length_less_than_8(self):
        self.assertEqual(check_string('Abc123'), ['String length should be atleast 8.'])

    def test_all_conditions(self):
        self.assertEqual(check_string('Abc12345'), ['Valid string.'])

    def test_empty_string(self):
        self.assertEqual(check_string(''), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])
