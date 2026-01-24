import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_empty_input(self):
        self.assertRaises(ValueError, binary_to_integer, ())

    def test_single_digit(self):
        self.assertEqual(binary_to_integer((1)), '1')

    def test_multiple_digits(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')

    def test_leading_zeros(self):
        self.assertEqual(binary_to_integer((0, 1, 0, 1)), '9')

    def test_trailing_zeros(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 0)), '11')

    def test_all_zeros(self):
        self.assertEqual(binary_to_integer((0,)), '0')

    def test_all_ones(self):
        self.assertEqual(binary_to_integer((1,) * 32), '4294967295')

    def test_negative_numbers(self):
        self.assertRaises(ValueError, binary_to_integer, ((1,) * 32) + (0,))

    def test_invalid_input(self):
        self.assertRaises(ValueError, binary_to_integer, (1.5,))
