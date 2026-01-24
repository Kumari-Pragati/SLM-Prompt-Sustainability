import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(float_to_tuple('1.2, 3.4, 5.6'), (1.2, 3.4, 5.6))

    def test_single_float(self):
        self.assertEqual(float_to_tuple('1.2'), (1.2,))

    def test_empty_string(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_negative_floats(self):
        self.assertEqual(float_to_tuple('-1.2, -3.4, -5.6'), (-1.2, -3.4, -5.6))

    def test_zero(self):
        self.assertEqual(float_to_tuple('0'), (0.0,))

    def test_large_floats(self):
        self.assertEqual(float_to_tuple('123456789.123456789'), (123456789.123456789,))

    def test_decimal_without_integer(self):
        self.assertEqual(float_to_tuple('.123'), (0.123,))

    def test_integer_without_decimal(self):
        self.assertEqual(float_to_tuple('123'), (123.0,))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('invalid')
