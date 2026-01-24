import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_empty_string(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_edge_case_single_element(self):
        self.assertEqual(float_to_tuple('1.0'), (1.0,))

    def test_edge_case_single_element_with_spaces(self):
        self.assertEqual(float_to_tuple(' 1.0  '), (1.0,))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(float_to_tuple('1.0,   2.0,   3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(float_to_tuple('-1.0, 2.0, -3.0'), (-1.0, 2.0, -3.0))

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0, 2.0, foo')

    def test_edge_case_non_numeric_input_with_spaces(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0, 2.0, foo bar')

    def test_edge_case_mixed_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0, 2.0, 3.0, foo')
