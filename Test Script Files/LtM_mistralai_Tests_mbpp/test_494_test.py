import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(binary_to_integer((1)), '1')
        self.assertEqual(binary_to_integer((1, 0)), '2')
        self.assertEqual(binary_to_integer((1, 0, 1)), '3')
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '4')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binary_to_integer((0)), '0')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1)), '63')
        self.assertEqual(binary_to_integer((0, 0, 0, 0, 0, 0)), '0')
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 1, 1, 1, 1)), '127')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1, 1)), '255')

    def test_complex_inputs(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 0, 1)), '13')
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 0, 1, 0)), '28')
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 0, 1, 0, 1)), '56')
        self.assertEqual(binary_to_integer((1, 0, 1, 1, 0, 1, 0, 1, 0)), '112')
