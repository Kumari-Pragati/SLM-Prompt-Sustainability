import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3))

    def test_single_number(self):
        self.assertEqual(tuple_str_int('4'), (4,))

    def test_empty_string(self):
        self.assertEqual(tuple_str_int(''), ())

    def test_negative_numbers(self):
        self.assertEqual(tuple_str_int('-1, -2, -3'), (-1, -2, -3))

    def test_zero(self):
        self.assertEqual(tuple_str_int('0'), (0,))

    def test_large_numbers(self):
        self.assertEqual(tuple_str_int('1000000, 2000000, 3000000'), (1000000, 2000000, 3000000))

    def test_decimal_numbers(self):
        self.assertEqual(tuple_str_int('1.1, 2.2, 3.3'), (1, 2, 3))

    def test_non_integer_strings(self):
        self.assertEqual(tuple_str_int('1.0, 2.0, 3.0'), (1, 2, 3))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_str_int('1, 2, three')

    def test_invalid_input_with_parentheses(self):
        with self.assertRaises(ValueError):
            tuple_str_int('(1, 2, 3)')

    def test_invalid_input_with_ellipsis(self):
        with self.assertRaises(ValueError):
            tuple_str_int('1...2...3')
