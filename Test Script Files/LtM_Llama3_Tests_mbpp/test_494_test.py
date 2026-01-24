import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            binary_to_integer(())

    def test_single_bit_input(self):
        self.assertEqual(binary_to_integer((1,)), '1')

    def test_max_value_input(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)), '32767')

    def test_max_value_input_with_leading_zeros(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)), '32767')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            binary_to_integer(['a', 1, 0, 1])
