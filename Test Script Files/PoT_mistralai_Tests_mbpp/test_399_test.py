import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))
        self.assertEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 0, 0))
        self.assertEqual(bitwise_xor((10, 20, 30), (40, 50, 60)), (50, 20, 90))

    def test_edge_cases(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(bitwise_xor((1, 0, 1), (0, 1, 0)), (1, 1, 2))
        self.assertEqual(bitwise_xor((255, 255, 255), (0, 0, 0)), (255, 255, 255))

    def test_corner_cases(self):
        self.assertEqual(bitwise_xor((1, 0, 1), (0, 1, 0, 1)), (1, 1, 0, 2))
        self.assertEqual(bitwise_xor((1,), (2,)), (3,))
        self.assertEqual(bitwise_xor((1, 2, 3, 4), (5, 6, 7, 8)), (4, 3, 1, 9))
