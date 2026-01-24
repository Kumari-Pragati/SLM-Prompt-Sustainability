import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_bitwise_xor_same_length_tuples(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 7, 5))

    def test_bitwise_xor_diff_length_tuples(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5)), (5, 7))

    def test_bitwise_xor_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_bitwise_xor_one_empty_tuple(self):
        self.assertEqual(bitwise_xor((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(bitwise_xor((1, 2, 3), ()), (1, 2, 3))

    def test_bitwise_xor_with_zero(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (0, 0, 0)), (1, 2, 3))
        self.assertEqual(bitwise_xor((0, 0, 0), (1, 2, 3)), (1, 2, 3))
