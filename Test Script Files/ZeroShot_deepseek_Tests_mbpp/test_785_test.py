import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3))

    def test_negative_numbers(self):
        self.assertEqual(tuple_str_int('-1, -2, -3'), (-1, -2, -3))

    def test_zero(self):
        self.assertEqual(tuple_str_int('0, 0, 0'), (0, 0, 0))

    def test_large_numbers(self):
        self.assertEqual(tuple_str_int('1000, 2000, 3000'), (1000, 2000, 3000))

    def test_empty_string(self):
        self.assertEqual(tuple_str_int(''), ())

    def test_single_number(self):
        self.assertEqual(tuple_str_int('1'), (1,))

    def test_float_numbers(self):
        self.assertEqual(tuple_str_int('1.5, 2.5, 3.5'), (1, 2, 3))

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            tuple_str_int('a, b, c')

    def test_non_comma_separated_string(self):
        with self.assertRaises(ValueError):
            tuple_str_int('1 2 3')
