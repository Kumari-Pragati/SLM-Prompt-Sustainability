import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0'), (1.0, 2.5, 3.0))

    def test_negative_numbers(self):
        self.assertTupleEqual(float_to_tuple('-1, -2.5, -3.0'), (-1.0, -2.5, -3.0))

    def test_zero(self):
        self.assertTupleEqual(float_to_tuple('0, 0.0, 0.0'), (0.0, 0.0, 0.0))

    def test_leading_trailing_whitespace(self):
        self.assertTupleEqual(float_to_tuple('  1,  2.5,  3.0   '), (1.0, 2.5, 3.0))

    def test_empty_string(self):
        self.assertIsInstance(float_to_tuple(''), tuple)
        self.assertIsNone(float_to_tuple(''), None)

    def test_invalid_input(self):
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3x')
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3, 4, 5, 6, 7, 8, 9, 10.1, 11.2, 12.3, 13.4, 14.5, 15.6, 16.7, 17.8, 18.9, 19.0, 20.1, 21.2, 22.3, 23.4, 24.5, 25.6, 26.7, 27.8, 28.9, 29.0, 30.1')
