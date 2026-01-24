import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3))

    def test_empty_string(self):
        self.assertEqual(tuple_str_int(''), ())

    def test_single_number(self):
        self.assertEqual(tuple_str_int('4'), (4,))

    def test_negative_numbers(self):
        self.assertEqual(tuple_str_int('-1, -2, -3'), (-1, -2, -3))

    def test_decimal_numbers(self):
        self.assertEqual(tuple_str_int('1.5, 2.5, 3.5'), (1, 2, 3))

    def test_edge_case_with_spaces(self):
        self.assertEqual(tuple_str_int(' 1 , 2 , 3 '), (1, 2, 3))

    def test_edge_case_with_parentheses(self):
        self.assertEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3))

    def test_edge_case_with_ellipsis(self):
        self.assertEqual(tuple_str_int('1...2...3'), (1, 2, 3))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_str_int('1, 2, three')
