import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 3, 1))

    def test_edge_condition_1(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 1, 1))

    def test_edge_condition_2(self):
        self.assertEqual(bitwise_xor((255, 255, 255), (0, 0, 0)), (255, 255, 255))

    def test_boundary_condition_1(self):
        self.assertEqual(bitwise_xor((-1, 0, 1), (0, 0, 0)), (-1, 0, 1))

    def test_boundary_condition_2(self):
        self.assertEqual(bitwise_xor((0, 0, 1), (1, 1, 1)), (0, 0, 0))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            bitwise_xor('abc', (1, 2, 3))

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), 'abc')
