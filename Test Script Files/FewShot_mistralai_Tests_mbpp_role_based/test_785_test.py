import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(tuple_str_int('(1, 2, 3, 4)'), (1, 2, 3, 4))
        self.assertEqual(tuple_str_int('(1, 2, 3, 4, 5)'), (1, 2, 3, 4, 5))
        self.assertEqual(tuple_str_int('(0, -1, 0, 1)'), (0, -1, 0, 1))

    def test_empty_input(self):
        self.assertEqual(tuple_str_int('()'), ())

    def test_single_element_input(self):
        self.assertEqual(tuple_str_int('(1)'), (1,))

    def test_invalid_input_no_parentheses(self):
        self.assertRaises(ValueError, tuple_str_int, '1, 2, 3')

    def test_invalid_input_no_commas(self):
        self.assertRaises(ValueError, tuple_str_int, '(123)')

    def test_invalid_input_no_numbers(self):
        self.assertRaises(ValueError, tuple_str_int, '(a, b, c)')

    def test_invalid_input_no_closing_parenthesis(self):
        self.assertRaises(ValueError, tuple_str_int, '(1, 2, 3)...')
