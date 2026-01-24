import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(float_to_tuple("1.0, 2.0, 3.0"), (1.0, 2.0, 3.0))

    def test_edge_boundary_conditions(self):
        self.assertEqual(float_to_tuple("0.0"), (0.0,))
        self.assertEqual(float_to_tuple("-1.0, 0.0, 1.0"), (-1.0, 0.0, 1.0))
        self.assertEqual(float_to_tuple("1.234567890123456789"), (1.234567890123456789,))

    def test_more_complex_cases(self):
        self.assertEqual(float_to_tuple("1.23, 4.56, 7.89, 0.12"), (1.23, 4.56, 7.89, 0.12))
        self.assertEqual(float_to_tuple("1.0, 2.0, 3.0, 4.0, 5.0"), (1.0, 2.0, 3.0, 4.0, 5.0))

    def test_empty_input(self):
        self.assertEqual(float_to_tuple(""), ())

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            float_to_tuple("invalid, input")
        with self.assertRaises(ValueError):
            float_to_tuple("1, 2, 3, invalid, 4")
