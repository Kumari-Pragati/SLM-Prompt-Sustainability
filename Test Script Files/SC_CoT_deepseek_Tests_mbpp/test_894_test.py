import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(float_to_tuple("1.2, 3.4, 5.6"), (1.2, 3.4, 5.6))

    def test_edge_case(self):
        self.assertEqual(float_to_tuple("0, 0, 0"), (0, 0, 0))

    def test_boundary_case(self):
        self.assertEqual(float_to_tuple("1.7976931348623157e+308, -1.7976931348623157e+308"), 
                         (float('inf'), -float('inf')))

    def test_special_case(self):
        self.assertEqual(float_to_tuple("NaN, inf, -inf"), (float('nan'), float('inf'), -float('inf')))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple("invalid, input")
