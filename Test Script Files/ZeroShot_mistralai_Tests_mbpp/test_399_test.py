import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXOR(unittest.TestCase):

    def test_bitwise_xor_simple(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))

    def test_bitwise_xor_zero(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 1, 0))

    def test_bitwise_xor_negative(self):
        self.assertEqual(bitwise_xor((-1, -2, -3), (-4, -5, -6)), (-5, -1, 7))

    def test_bitwise_xor_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_bitwise_xor_different_lengths(self):
        with self.assertRaises(ValueError):
            bitwise_xor((1, 2, 3), (1, 2))
