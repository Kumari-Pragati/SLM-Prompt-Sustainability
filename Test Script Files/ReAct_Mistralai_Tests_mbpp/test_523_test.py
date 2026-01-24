import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_string("ValidString123"), ['Valid string.'])
        self.assertEqual(check_string("ValidString1234567"), ['Valid string.'])

    def test_min_length(self):
        self.assertEqual(check_string("ValidStr"), ['String length should be atleast 8.'])
        self.assertEqual(check_string("ValidString"), ['String length should be atleast 8.'])

    def test_upper_case(self):
        self.assertEqual(check_string("ValidStr123"), ['String must have 1 upper case character.'])
        self.assertEqual(check_string("ValidStr1234567"), ['Valid string.'])

    def test_lower_case(self):
        self.assertEqual(check_string("VALIDSTR123"), ['String must have 1 lower case character.'])
        self.assertEqual(check_string("ValidStr1234567"), ['Valid string.'])

    def test_number(self):
        self.assertEqual(check_string("ValidStr12345"), ['String must have 1 number.'])
        self.assertEqual(check_string("ValidStr1234567"), ['Valid string.'])

    def test_special_characters(self):
        self.assertEqual(check_string("ValidStr!123"), check_string("ValidStr123"))
        self.assertEqual(check_string("ValidStr$123"), check_string("ValidStr123"))
        self.assertEqual(check_string("ValidStr@123"), check_string("ValidStr123"))
        self.assertEqual(check_string("ValidStr_123"), check_string("ValidStr123"))

    def test_multiple_errors(self):
        self.assertEqual(check_string("ValidStr"), ['String length should be atleast 8.', 'String must have 1 upper case character.', 'String must have 1 lower case character.'])
        self.assertEqual(check_string("ValidStr12345"), ['String must have 1 number.', 'String length should be atleast 8.'])
