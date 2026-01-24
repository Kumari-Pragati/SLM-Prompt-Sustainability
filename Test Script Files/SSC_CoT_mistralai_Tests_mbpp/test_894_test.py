import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0'), (1.0, 2.5, 3.0))
        self.assertTupleEqual(float_to_tuple('-1, 0, 1'), (-1.0, 0.0, 1.0))

    def test_edge_cases(self):
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0, 0'), (1.0, 2.5, 3.0, 0.0))
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0, 0, 0'), (1.0, 2.5, 3.0, 0.0, 0.0))
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0, 0, 0, 0'), (1.0, 2.5, 3.0, 0.0, 0.0, 0.0))

    def test_boundary_cases(self):
        self.assertTupleEqual(float_to_tuple('-1, -0.5, 0, 0.5, 1'), (-1.0, -0.5, 0.0, 0.0, 1.0))
        self.assertTupleEqual(float_to_tuple('-1e-20, -0.5, 0, 0.5, 1'), (-1e-20, -0.5, 0.0, 0.5, 1.0))
        self.assertTupleEqual(float_to_tuple('-1e20, -0.5, 0, 0.5, 1'), (-1e20, -0.5, 0.0, 0.5, 1.0))

    def test_invalid_input(self):
        self.assertRaises(ValueError, float_to_tuple, 'invalid_string')
        self.assertRaises(ValueError, float_to_tuple, '1, invalid_number, 3.0')
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3, invalid_number')
