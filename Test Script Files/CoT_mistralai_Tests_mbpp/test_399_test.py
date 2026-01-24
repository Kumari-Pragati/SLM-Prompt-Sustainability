import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_bitwise_xor_typical_inputs(self):
        self.assertTupleEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))
        self.assertTupleEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 0, 0))
        self.assertTupleEqual(bitwise_xor((10, 20, 30), (40, 50, 60)), (50, 20, 90))

    def test_bitwise_xor_edge_cases(self):
        self.assertTupleEqual(bitwise_xor((0,), (1,)), (1,))
        self.assertTupleEqual(bitwise_xor((1,), (0,)), (1,))
        self.assertTupleEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertTupleEqual(bitwise_xor((255, 255, 255), (255, 255, 255)), (0, 0, 0))

    def test_bitwise_xor_invalid_inputs(self):
        self.assertRaises(TypeError, bitwise_xor, (1, 2, 3), "not_a_tuple")
        self.assertRaises(TypeError, bitwise_xor, [1, 2, 3], (4, 5, 6))
