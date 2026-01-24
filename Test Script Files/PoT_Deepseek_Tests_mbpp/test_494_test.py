import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')

    def test_edge_cases(self):
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1)), '31')

    def test_boundary_conditions(self):
        self.assertEqual(binary_to_integer((2,)), '2')
        self.assertEqual(binary_to_integer((1, 0)), '2')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_integer((1, 'a'))
        with self.assertRaises(TypeError):
            binary_to_integer((1, 2))
        with self.assertRaises(TypeError):
            binary_to_integer((1, 0.5))
