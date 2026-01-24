import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_valid_binary(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), "5")

    def test_binary_with_leading_zeros(self):
        self.assertEqual(binary_to_integer((0, 0, 1)), "1")

    def test_binary_with_trailing_zeros(self):
        self.assertEqual(binary_to_integer((1, 0, 0, 0)), "4")

    def test_binary_with_multiple_zeros(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 1)), "1")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            binary_to_integer("invalid_input")

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            binary_to_integer(())
