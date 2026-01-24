import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_string('abcD12345'), ['Valid string.'])

    def test_no_uppercase(self):
        self.assertEqual(check_string('abcd12345'), 
                         ['String must have 1 upper case character.'])

    def test_no_lowercase(self):
        self.assertEqual(check_string('ABCDEFGH'), 
                         ['String must have 1 lower case character.'])

    def test_no_digit(self):
        self.assertEqual(check_string('ABCDEFGH'), 
                         ['String must have 1 number.'])

    def test_length_less_than_8(self):
        self.assertEqual(check_string('abcD123'), 
                         ['String length should be atleast 8.'])

    def test_all_conditions(self):
        self.assertEqual(check_string('abcD12345'), 
                         ['Valid string.'])
        self.assertEqual(check_string('abc12345'), 
                         ['String must have 1 upper case character.'])
        self.assertEqual(check_string('ABCDEFGH'), 
                         ['String must have 1 lower case character.'])
        self.assertEqual(check_string('ABCDEFGH'), 
                         ['String must have 1 number.'])
        self.assertEqual(check_string('ABCDEFGH'), 
                         ['String length should be atleast 8.'])
