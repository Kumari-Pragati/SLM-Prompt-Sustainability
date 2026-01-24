import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_valid_binary_numbers(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '11')
        self.assertEqual(binary_to_integer((0, 1, 1, 0, 1, 1, 0, 1)), '11101101')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1)), '255')

    def test_empty_list(self):
        self.assertEqual(binary_to_integer([]), '')

    def test_single_element(self):
        self.assertEqual(binary_to_integer((0)), '0')
        self.assertEqual(binary_to_integer((1)), '1')

    def test_all_zeros(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')

    def test_all_ones(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')

    def test_long_binary_number(self):
        self.assertEqual(binary_to_integer((0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)), '1101101101101101')

    def test_invalid_input(self):
        self.assertRaises(ValueError, binary_to_integer, (1, 'a'))
        self.assertRaises(ValueError, binary_to_integer, (1, 2))
