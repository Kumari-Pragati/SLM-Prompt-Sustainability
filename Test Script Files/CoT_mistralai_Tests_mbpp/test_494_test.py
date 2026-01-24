import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 0)), '12')
        self.assertEqual(binary_to_integer((0, 1, 1, 0, 1, 0, 1, 1)), '135')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1)), '255')

    def test_edge_cases(self):
        self.assertEqual(binary_to_integer((0,)), '0')
        self.assertEqual(binary_to_integer((1)), '1')
        self.assertEqual(binary_to_integer((0, 0, 0, 0, 0, 0, 0, 0)), '0')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1, 1)), '255')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, binary_to_integer, (1, 'a'))
        self.assertRaises(ValueError, binary_to_integer, ())
        self.assertRaises(ValueError, binary_to_integer, (1, 2, 3))
