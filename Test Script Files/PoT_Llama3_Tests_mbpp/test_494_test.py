import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '3')

    def test_edge_case_all_ones(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')

    def test_edge_case_all_zeros(self):
        self.assertEqual(binary_to_integer((0, 0, 0)), '0')

    def test_edge_case_single_bit(self):
        self.assertEqual(binary_to_integer((1)), '1')

    def test_edge_case_empty_input(self):
        with self.assertRaises(TypeError):
            binary_to_integer(())

    def test_edge_case_non_binary_input(self):
        with self.assertRaises(ValueError):
            binary_to_integer((1, 2, 3))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_integer('abc')
