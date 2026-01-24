import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4'), (1, 2, 3, 4))

    def test_empty_string(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_single_number(self):
        self.assertEqual(str_to_tuple('5'), (5,))

    def test_multiple_spaces(self):
        self.assertEqual(str_to_tuple('1  , 2  , 3  , 4'), (1, 2, 3, 4))

    def test_no_comma(self):
        self.assertEqual(str_to_tuple('1 2 3 4'), (1, 2, 3, 4))

    def test_negative_numbers(self):
        self.assertEqual(str_to_tuple('-1, -2, -3, -4'), (-1, -2, -3, -4))

    def test_float_numbers(self):
        self.assertEqual(str_to_tuple('1.5, 2.5, 3.5, 4.5'), (1.5, 2.5, 3.5, 4.5))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, 2, 3, a')
