import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4'), (1, 2, 3, 4))

    def test_single_number(self):
        self.assertEqual(str_to_tuple('5'), (5,))

    def test_empty_string(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_negative_numbers(self):
        self.assertEqual(str_to_tuple('-1, -2, -3, -4'), (-1, -2, -3, -4))

    def test_zero(self):
        self.assertEqual(str_to_tuple('0'), (0,))

    def test_large_numbers(self):
        self.assertEqual(str_to_tuple('1000000, 2000000, 3000000'), (1000000, 2000000, 3000000))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, 2, 3, a')

    def test_whitespace_in_input(self):
        self.assertEqual(str_to_tuple('1,  2,  3,  4'), (1, 2, 3, 4))
