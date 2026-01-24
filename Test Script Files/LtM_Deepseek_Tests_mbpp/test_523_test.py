import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_simple_valid_string(self):
        self.assertEqual(check_string('aB1'), ['Valid string.'])

    def test_missing_uppercase(self):
        self.assertEqual(check_string('ab1'), ['String must have 1 upper case character.'])

    def test_missing_lowercase(self):
        self.assertEqual(check_string('AB1'), ['String must have 1 lower case character.'])

    def test_missing_digit(self):
        self.assertEqual(check_string('ABab'), ['String must have 1 number.'])

    def test_length_less_than_8(self):
        self.assertEqual(check_string('ABa1'), ['String length should be atleast 8.'])

    def test_empty_string(self):
        self.assertEqual(check_string(''), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])

    def test_all_conditions_met(self):
        self.assertEqual(check_string('Ab123456'), ['Valid string.'])
