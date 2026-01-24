import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertRaises(ValueError, float_to_tuple, '')

    def test_single_float(self):
        result = float_to_tuple('3.14')
        self.assertEqual(result, (3.14,))

    def test_multiple_floats_no_comma(self):
        result = float_to_tuple('1.2 3.4 5.6')
        self.assertEqual(result, (1.2, 3.4, 5.6))

    def test_multiple_floats_with_comma(self):
        result = float_to_tuple('1.2, 3.4, 5.6')
        self.assertEqual(result, (1.2, 3.4, 5.6))

    def test_multiple_floats_with_extra_spaces(self):
        result = float_to_tuple('  1.2 ,  3.4  ,  5.6  ')
        self.assertEqual(result, (1.2, 3.4, 5.6))

    def test_invalid_float(self):
        self.assertRaises(ValueError, float_to_tuple, 'invalid float')

    def test_leading_trailing_whitespace(self):
        result = float_to_tuple('  1.2 ,  3.4  ,  5.6  ')
        self.assertEqual(result, (1.2, 3.4, 5.6))

    def test_negative_floats(self):
        result = float_to_tuple('-1.2, -3.4, -5.6')
        self.assertEqual(result, (-1.2, -3.4, -5.6))
