import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_simple_binary_to_integer(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')
        self.assertEqual(binary_to_integer((1, 1, 1)), '7')
        self.assertEqual(binary_to_integer((0, 0, 0)), '0')

    def test_edge_conditions(self):
        self.assertEqual(binary_to_integer(()), '0')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 1)), '255')

    def test_complex_cases(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 0, 1, 0, 1, 0)), '210')
        self.assertEqual(binary_to_integer((1, 1, 1, 1, 1, 1, 1, 0)), '254')
