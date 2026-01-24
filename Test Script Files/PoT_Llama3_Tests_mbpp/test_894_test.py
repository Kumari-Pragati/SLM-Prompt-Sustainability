import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_empty_input(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_edge_case_single_element(self):
        self.assertEqual(float_to_tuple('1.0'), (1.0,))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(float_to_tuple(' 1.0, 2.0, 3.0  '), (1.0, 2.0, 3.0))

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(float_to_tuple(' 1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_comma_at_end(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0,'), (1.0, 2.0, 3.0))

    def test_edge_case_comma_at_start(self):
        self.assertEqual(float_to_tuple(', 1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_edge_case_multiple_commas(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0, 4.0, 5.0'), (1.0, 2.0, 3.0, 4.0, 5.0))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('1.0, 2.0, invalid')
