import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_upper_case(self):
        self.assertEqual(check_string('abc'), ['String must have 1 upper case character.'])
        self.assertEqual(check_string('ABC'), ['Valid string.'])

    def test_lower_case(self):
        self.assertEqual(check_string('ABC'), ['String must have 1 lower case character.'])
        self.assertEqual(check_string('abc'), ['Valid string.'])

    def test_digit(self):
        self.assertEqual(check_string('abc'), ['String must have 1 number.'])
        self.assertEqual(check_string('123'), ['Valid string.'])

    def test_length(self):
        self.assertEqual(check_string('abc'), ['String length should be atleast 8.'])
        self.assertEqual(check_string('abcdefgh'), ['Valid string.'])

    def test_all_conditions(self):
        self.assertEqual(check_string('abc123'), ['String must have 1 upper case character.', 
                                                  'String must have 1 lower case character.', 
                                                  'String length should be atleast 8.'])
        self.assertEqual(check_string('Abc123Abc'), ['Valid string.'])
