import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsInstance(tuple_str_int(''), tuple)
        self.assertListEqual(tuple_str_int(''), [])

    def test_single_element(self):
        self.assertIsInstance(tuple_str_int('1'), tuple)
        self.assertListEqual(tuple_str_int('1'), [1])

    def test_multiple_elements(self):
        self.assertIsInstance(tuple_str_int('1, 2, 3'), tuple)
        self.assertListEqual(tuple_str_int('1, 2, 3'), [1, 2, 3])

    def test_leading_trailing_spaces(self):
        self.assertIsInstance(tuple_str_int('  1,  2,  3   '), tuple)
        self.assertListEqual(tuple_str_int('  1,  2,  3   '), [1, 2, 3])

    def test_leading_trailing_parentheses(self):
        self.assertIsInstance(tuple_str_int('(1, 2, 3)'), tuple)
        self.assertListEqual(tuple_str_int('(1, 2, 3)'), [1, 2, 3])

    def test_leading_trailing_ellipsis(self):
        self.assertIsInstance(tuple_str_int('...1, 2, 3...'), tuple)
        self.assertListEqual(tuple_str_int('...1, 2, 3...'), [1, 2, 3])

    def test_invalid_input_no_comma(self):
        self.assertRaises(ValueError, tuple_str_int, '12(3)')

    def test_invalid_input_non_numeric(self):
        self.assertRaises(ValueError, tuple_str_int, '1a, 2, 3')

    def test_invalid_input_empty_element(self):
        self.assertRaises(ValueError, tuple_str_int, '1,,3')
