import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_single_float(self):
        self.assertEqual(float_to_tuple('1.23'), (1.23,))

    def test_multiple_floats(self):
        self.assertEqual(float_to_tuple('1.23, 4.56, 7.89'), (1.23, 4.56, 7.89))

    def test_zero(self):
        self.assertEqual(float_to_tuple('0'), (0.0,))

    def test_negative_floats(self):
        self.assertEqual(float_to_tuple('-1.23, -4.56, -7.89'), (-1.23, -4.56, -7.89))

    def test_empty_string(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_whitespace_in_string(self):
        self.assertEqual(float_to_tuple(' 1.23, 4.56, 7.89 '), (1.23, 4.56, 7.89))
