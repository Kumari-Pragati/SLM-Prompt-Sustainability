import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertRaises(ValueError, str_to_tuple, '')

    def test_single_element(self):
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_multiple_elements(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4'), (1, 2, 3, 4))

    def test_leading_trailing_whitespace(self):
        self.assertEqual(str_to_tuple('  1, 2, 3,  4   '), (1, 2, 3, 4))

    def test_comma_separator(self):
        self.assertEqual(str_to_tuple('1,2,3,4'), (1, 2, 3, 4))

    def test_semicolon_separator(self):
        self.assertRaises(ValueError, str_to_tuple, '1;2;3;4')

    def test_space_separator(self):
        self.assertRaises(ValueError, str_to_tuple, '1 2 3 4')

    def test_invalid_element(self):
        self.assertRaises(ValueError, str_to_tuple, '1, x, 3, 4')

    def test_negative_numbers(self):
        self.assertEqual(str_to_tuple('-1, 0, 1, 2'), (-1, 0, 1, 2))
