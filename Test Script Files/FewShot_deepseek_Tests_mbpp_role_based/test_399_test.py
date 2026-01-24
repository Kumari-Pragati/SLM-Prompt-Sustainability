import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 7, 5))

    def test_boundary_conditions(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(bitwise_xor((255, 255, 255), (0, 0, 0)), (255, 255, 255))

    def test_different_lengths(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5)), (5, 7))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), "4, 5, 6")
        with self.assertRaises(TypeError):
            bitwise_xor("1, 2, 3", (4, 5, 6))
