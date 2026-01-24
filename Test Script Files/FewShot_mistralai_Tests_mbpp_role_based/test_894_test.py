import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(float_to_tuple("1.2, 3.4, 5.6"), (1.2, 3.4, 5.6))
        self.assertEqual(float_to_tuple("0.0, 0.0, 0.0"), (0.0, 0.0, 0.0))

    def test_empty_input(self):
        self.assertRaises(ValueError, float_to_tuple, "")

    def test_single_input(self):
        self.assertRaises(ValueError, float_to_tuple, "1.2")

    def test_invalid_input(self):
        self.assertRaises(ValueError, float_to_tuple, "1.2, 3, 5.6")
