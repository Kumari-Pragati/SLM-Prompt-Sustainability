import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertTupleEqual(float_to_tuple("1, 2, 3"), (1.0, 2.0, 3.0))

    def test_negative_numbers(self):
        self.assertTupleEqual(float_to_tuple("-1, 0, 3"), (-1.0, 0.0, 3.0))

    def test_floats_with_decimals(self):
        self.assertTupleEqual(float_to_tuple("1.5, 2.75, 3.14"), (1.5, 2.75, 3.14))

    def test_empty_string(self):
        self.assertIsInstance(float_to_tuple(""), tuple)
        self.assertIsInstance(float_to_tuple(""), tuple, "Expected empty tuple.")

    def test_single_value(self):
        self.assertTupleEqual(float_to_tuple("1"), (1.0,))

    def test_comma_missing(self):
        self.assertIsInstance(float_to_tuple("1 2 3"), tuple)
        self.assertNotEqual(float_to_tuple("1 2 3"), (1.0, 2.0, 3.0))

    def test_whitespace_around_comma(self):
        self.assertTupleEqual(float_to_tuple(" 1 , 2 , 3 "), (1.0, 2.0, 3.0))
