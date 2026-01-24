import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(binary_to_integer((1, 0, 1)), '5')
        self.assertEqual(binary_to_integer((1, 1, 1)), '7')
        self.assertEqual(binary_to_integer((0, 1, 0)), '2')

    def test_edge_cases(self):
        self.assertEqual(binary_to_integer((1)), '1')
        self.assertEqual(binary_to_integer((0)), '0')
        self.assertEqual(binary_to_integer(()), '0')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_integer('test')
        with self.assertRaises(TypeError):
            binary_to_integer([1, 2, 3])

    def test_corner_cases(self):
        self.assertEqual(binary_to_integer((1, 1)), '3')
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '11')
