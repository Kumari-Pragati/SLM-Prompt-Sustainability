import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_string_with_upper_case(self):
        self.assertIn('Valid string.', check_string('TestString'))

    def test_string_without_upper_case(self):
        self.assertIn('String must have 1 upper case character.', check_string('teststring'))

    def test_string_with_lower_case(self):
        self.assertIn('Valid string.', check_string('Testtest'))

    def test_string_without_lower_case(self):
        self.assertIn('String must have 1 lower case character.', check_string('TESTTEST'))

    def test_string_with_number(self):
        self.assertIn('Valid string.', check_string('Test123'))

    def test_string_without_number(self):
        self.assertIn('String must have 1 number.', check_string('TestTest'))

    def test_string_with_length_less_than_8(self):
        self.assertIn('String length should be atleast 8.', check_string('Test'))

    def test_string_with_length_greater_than_8(self):
        self.assertIn('Valid string.', check_string('TestString1234'))
