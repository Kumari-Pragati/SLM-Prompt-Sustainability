import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string('ValidString'), ['Valid string.'])
        self.assertEqual(check_string('ValidString123'), ['Valid string.'])
        self.assertEqual(check_string('ValidString123_'), ['Valid string.'])
        self.assertEqual(check_string('ValidString123_456'), ['Valid string.'])

    def test_min_length(self):
        self.assertEqual(check_string('ShortString'), ['String length should be atleast 8.'])
        self.assertEqual(check_string('ShortString1'), ['String length should be atleast 8.'])

    def test_upper_case(self):
        self.assertEqual(check_string('alllowercase'), ['String must have 1 upper case character.'])
        self.assertEqual(check_string('AllLowercase'), ['Valid string.'])
        self.assertEqual(check_string('AllLowerCase'), ['String must have 1 upper case character.'])

    def test_lower_case(self):
        self.assertEqual(check_string('ALLUPPERCASE'), ['String must have 1 lower case character.'])
        self.assertEqual(check_string('AllUpperCase'), ['Valid string.'])
        self.assertEqual(check_string('AllUpper CAsE'), ['String must have 1 lower case character.'])

    def test_numbers(self):
        self.assertEqual(check_string('1234567'), ['String must have 1 number.'])
        self.assertEqual(check_string('12345678'), ['Valid string.'])
        self.assertEqual(check_string('1234567A'), ['Valid string.'])

    def test_special_characters(self):
        self.assertEqual(check_string('ValidString!'), ['Valid string.'])
        self.assertEqual(check_string('ValidString@'), ['Valid string.'])
        self.assertEqual(check_string('ValidString#'), ['Valid string.'])

    def test_invalid_inputs(self):
        self.assertEqual(check_string(123), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.', 'String length should be atleast 8.'])
        self.assertEqual(check_string(''), ['String length should be atleast 8.'])
        self.assertEqual(check_string(' '), ['String length should be atleast 8.'])
        self.assertEqual(check_string('123456789'), ['Valid string.'])
