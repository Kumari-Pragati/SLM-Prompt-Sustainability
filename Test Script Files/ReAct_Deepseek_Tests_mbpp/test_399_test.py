import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 7, 5))

    def test_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_different_length_tuples(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5)), (5, 7))

    def test_zero_values(self):
        self.assertEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_negative_values(self):
        self.assertEqual(bitwise_xor((-1, -2, -3), (-4, -5, -6)), (-5, -7, -5))

    def test_large_numbers(self):
        self.assertEqual(bitwise_xor((1000000000, 2000000000), (3000000000, 4000000000)), 
                         (3000000000, 6000000000))
