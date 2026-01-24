import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_string('ValidString'), ['Valid string.'])
        self.assertEqual(check_string('ValidStrInG'), ['Valid string.'])
        self.assertEqual(check_string('Valid1StrInG'), ['Valid string.'])
        self.assertEqual(check_string('ValidStrInG1'), ['Valid string.'])

    def test_minimal_string(self):
        self.assertEqual(check_string('Ab1'), ['String length should be atleast 8.'])
        self.assertEqual(check_string('Ab1c'), ['String length should be atleast 8.'])
        self.assertEqual(check_string('Ab1cD'), ['String length should be atleast 8.'])

    def test_uppercase_edge_case(self):
        self.assertEqual(check_string('ABCDEFGHIJ'), ['String must have 1 lower case character.'])
        self.assertEqual(check_string('ABCDEFGHIJK'), ['String must have 1 lower case character.'])

    def test_lowercase_edge_case(self):
        self.assertEqual(check_string('abcdefghij'), ['String must have 1 upper case character.'])
        self.assertEqual(check_string('abcdefghijAB'), ['String must have 1 upper case character.'])

    def test_digit_edge_case(self):
        self.assertEqual(check_string('Ab1cD2'), ['String must have 1 non-digit character.'])
        self.assertEqual(check_string('Ab1cD2E'), ['String must have 1 non-digit character.'])

    def test_invalid_input(self):
        self.assertEqual(check_string(123), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.'])
        self.assertEqual(check_string(''), ['String length should be atleast 8.'])
        self.assertEqual(check_string(' '), ['String length should be atleast 8.'])
        self.assertEqual(check_string('A'), ['String must have 1 lower case character.'])
        self.assertEqual(check_string('a'), ['String must have 1 upper case character.'])
        self.assertEqual(check_string('1'), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])
