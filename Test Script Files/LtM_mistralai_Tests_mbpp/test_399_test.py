import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))
        self.assertEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 0, 0))
        self.assertEqual(bitwise_xor((-1, 0, 1), (1, -1, 0)), (0, 0, 1))

    def test_edge_and_boundary(self):
        self.assertEqual(bitwise_xor((0,), (1,)), (1,))
        self.assertEqual(bitwise_xor((0, 0, 0, 0), (1, 1, 1, 1)), (1, 1, 1, 0))
        self.assertEqual(bitwise_xor((2**31 - 1,), (2**31 - 1,)), (0,))

    def test_complex(self):
        self.assertEqual(bitwise_xor((1, 0, 1, 0, 1, 0, 1, 0),
                                      (0, 1, 0, 1, 0, 1, 0, 1)),
                         (1, 1, 0, 0, 1, 1, 0, 0))
        self.assertEqual(bitwise_xor((-1, 0, 1), (1, -1, 0)), (0, 0, 1))
