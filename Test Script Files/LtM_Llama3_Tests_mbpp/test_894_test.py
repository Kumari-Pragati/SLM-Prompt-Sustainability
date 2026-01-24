import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(float_to_tuple('1, 2, 3'), (1.0, 2.0, 3.0))

    def test_empty_input(self):
        self.assertEqual(float_to_tuple(''), ())

    def test_single_element_input(self):
        self.assertEqual(float_to_tuple('1'), (1.0,))

    def test_multiple_elements_input(self):
        self.assertEqual(float_to_tuple('1, 2, 3, 4, 5'), (1.0, 2.0, 3.0, 4.0, 5.0))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            float_to_tuple('abc')

    def test_mixed_input(self):
        self.assertEqual(float_to_tuple('1, abc, 3, 4, 5'), (1.0, 3.0, 4.0, 5.0))

    def test_negative_input(self):
        self.assertEqual(float_to_tuple('-1, 2, 3'), (-1.0, 2.0, 3.0))

    def test_max_value_input(self):
        self.assertEqual(float_to_tuple('1.7976931348623157e+308'), (1.7976931348623157e+308,))

    def test_min_value_input(self):
        self.assertEqual(float_to_tuple('-1.7976931348623157e+308'), (-1.7976931348623157e+308,))
