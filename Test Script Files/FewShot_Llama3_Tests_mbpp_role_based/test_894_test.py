import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0'), (1.0, 2.0, 3.0))

    def test_empty_input(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_single_value_input(self):
        self.assertEqual(float_to_tuple('1.0'), (1.0,))

    def test_multiple_values_with_spaces(self):
        self.assertEqual(float_to_tuple('1.0, 2.0, 3.0, 4.0'), (1.0, 2.0, 3.0, 4.0))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('not a float')
