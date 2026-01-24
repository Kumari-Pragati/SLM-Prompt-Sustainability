import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_empty_string(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_edge_case_single_element(self):
        self.assertEqual(float_to_tuple('1.0'), (1.0,))

    def test_edge_case_multiple_elements(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0, 4.0, 5.0'), (1.0, 2.0, 3.0, 4.0, 5.0))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0, 2.0, invalid')

    def test_edge_case_missing_comma(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0 2.0')

    def test_edge_case_missing_space(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0,2.0')

    def test_edge_case_missing_comma_and_space(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0,2.0,3.0')
