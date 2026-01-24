import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 0)), '12')
        self.assertEqual(binary_to_integer((0, 1, 1, 0)), '10')
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(binary_to_integer((0,)), '0')
        self.assertEqual(binary_to_integer((1, 0, 0, 0, 0)), '12')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1)), '31')
        self.assertEqual(binary_to_integer((0, 0, 0, 0, 0)), '0')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, binary_to_integer, (1, 'a'))
        self.assertRaises(ValueError, binary_to_integer, (1, 3))
