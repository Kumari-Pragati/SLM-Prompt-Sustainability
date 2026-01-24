import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '7')

    def test_boundary_case(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '8')

    def test_edge_case(self):
        self.assertEqual(binary_to_integer((1,)), '1')
        self.assertEqual(binary_to_integer((0,)), '0')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_integer((2, 0, 1, 1))
        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, 1, '1'))
        with self.assertRaises(TypeError):
            binary_to_integer((1, 0, 1, 2))
