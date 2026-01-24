import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsInstance(float_to_tuple(''), tuple)
        self.assertListEqual(float_to_tuple(''), ())

    def test_single_float(self):
        self.assertIsInstance(float_to_tuple('3.14'), tuple)
        self.assertListEqual(float_to_tuple('3.14'), (3.14,))

    def test_multiple_floats(self):
        self.assertIsInstance(float_to_tuple('1.23, 4.56, 7.89'), tuple)
        self.assertListEqual(float_to_tuple('1.23, 4.56, 7.89'), (1.23, 4.56, 7.89))

    def test_invalid_input(self):
        self.assertRaises(ValueError, float_to_tuple, 'invalid input')

    def test_whitespace_around_comma(self):
        self.assertIsInstance(float_to_tuple(' 1.23 , 4.56 , 7.89 '), tuple)
        self.assertListEqual(float_to_tuple(' 1.23 , 4.56 , 7.89 '), (1.23, 4.56, 7.89))

    def test_leading_trailing_whitespace(self):
        self.assertIsInstance(float_to_tuple(' 1.23 , 4.56 , 7.89 '), tuple)
        self.assertListEqual(float_to_tuple(' 1.23 , 4.56 , 7.89 '), (1.23, 4.56, 7.89))
