import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (3, 7, 1))

    def test_edge_cases(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(bitwise_xor((1, 1, 1), (1, 1, 1)), (0, 0, 0))

    def test_boundary_cases(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (3, 2, 1)), (0, 0, 2))
        self.assertEqual(bitwise_xor((1, 1, 1), (1, 1, 1)), (0, 0, 0))

    def test_special_cases(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (3, 2, 1)), (0, 0, 2))
        self.assertEqual(bitwise_xor((1, 1, 1), (1, 1, 1)), (0, 0, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            bitwise_xor(None, (1, 2, 3))
        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), None)
        with self.assertRaises(TypeError):
            bitwise_xor(None, None)
