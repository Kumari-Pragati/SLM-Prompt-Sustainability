import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_bitwise_xor(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (3, 2, 1)), (0, 0, 2))
        self.assertEqual(bitwise_xor((1, 2, 3), (1, 2, 3)), (0, 0, 0))
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (3, 7, 7))
        self.assertEqual(bitwise_xor((), ()), ())
        self.assertEqual(bitwise_xor((1, 2), (3, 4)), (2, 6))
        self.assertEqual(bitwise_xor((1, 2, 3, 4), (5, 6, 7, 8)), (4, 6, 6, 8))

    def test_bitwise_xor_empty(self):
        self.assertEqual(bitwise_xor((), (1, 2, 3)), ())
        self.assertEqual(bitwise_xor((1, 2, 3), ()), ())
