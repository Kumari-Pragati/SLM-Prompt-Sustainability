import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(check_string('aB1234567'), ['Valid string.'])

    def test_no_uppercase(self):
        self.assertEqual(check_string('ab1234567'), ['String must have 1 upper case character.'])

    def test_no_lowercase(self):
        self.assertEqual(check_string('AB1234567'), ['String must have 1 lower case character.'])

    def test_no_digit(self):
        self.assertEqual(check_string('ABabABAB'), ['String must have 1 number.'])

    def test_length_less_than_8(self):
        self.assertEqual(check_string('ABabABA'), ['String length should be atleast 8.'])

    def test_no_uppercase_no_lowercase(self):
        self.assertEqual(check_string('12345678'), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])

    def test_no_uppercase_no_digit(self):
        self.assertEqual(check_string('abababab'), ['String must have 1 upper case character.', 'String must have 1 number.'])

    def test_no_lowercase_no_digit(self):
        self.assertEqual(check_string('ABABABAB'), ['String must have 1 lower case character.', 'String must have 1 number.'])

    def test_no_uppercase_no_lowercase_no_digit(self):
        self.assertEqual(check_string('ABCDEFGH'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_string(12345678)
