import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '7')

    def test_edge_case_single_bit(self):
        self.assertEqual(binary_to_integer((1)), '1')
        self.assertEqual(binary_to_integer((0)), '0')

    def test_edge_case_multiple_zeroes(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')

    def test_edge_case_multiple_ones(self):
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')

    def test_error_case_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, '1', 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, 2, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, None, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, [], 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, {}, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, set(), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, (), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, 0.5, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, True, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, False, 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, complex(1, 1), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, float('nan'), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, float('inf'), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, float('-inf'), 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, '', 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, 'a', 1))

        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, '1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101