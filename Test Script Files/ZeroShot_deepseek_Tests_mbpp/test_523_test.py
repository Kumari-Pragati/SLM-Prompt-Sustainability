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
        self.assertEqual(check_string('abcABC'), ['String must have 1 number.'])
        self.assertEqual(check_string('abcABC1'), ['Valid string.'])

    def test_length(self):
        self.assertEqual(check_string('abcABC1'), ['String length should be atleast 8.'])
        self.assertEqual(check_string('abcABC12345678'), ['Valid string.'])

    def test_all(self):
        self.assertEqual(check_string('abcABC1'), ['String must have 1 upper case character.', 
                                                   'String must have 1 lower case character.', 
                                                   'String must have 1 number.', 
                                                   'String length should be atleast 8.'])
        self.assertEqual(check_string('abcABC12345678'), ['Valid string.'])
