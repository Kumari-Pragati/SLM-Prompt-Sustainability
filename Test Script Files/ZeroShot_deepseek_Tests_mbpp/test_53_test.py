import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')

    def test_not_equal_strings(self):
        self.assertEqual(check_Equality('abcde'), 'Not Equal')

    def test_single_char_string(self):
        self.assertEqual(check_Equality('a'), 'Equal')

    def test_empty_string(self):
        self.assertEqual(check_Equality(''), 'Not Equal')

    def test_string_with_spaces(self):
        self.assertEqual(check_Equality('abc cba'), 'Equal')
