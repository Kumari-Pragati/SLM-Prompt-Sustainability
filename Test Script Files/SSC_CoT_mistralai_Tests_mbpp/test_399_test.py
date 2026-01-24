import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXOR(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertTupleEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))
        self.assertTupleEqual(bitwise_xor((0, 0, 0), (1, 1, 1)), (1, 0, 0))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(bitwise_xor((0, 0, 0, 0), (1, 0, 0, 0)), (1, 0, 0, 0))
        self.assertTupleEqual(bitwise_xor((1, 0, 0, 0), (0, 1, 0, 0)), (1, 0, 0, 0))
        self.assertTupleEqual(bitwise_xor((-1, 0, 0, 0), (0, -1, 0, 0)), (1, 1, 0, 0))
        self.assertTupleEqual(bitwise_xor((0, -1, 0, 0), (0, 1, 0, 0)), (1, 1, 0, 0))
        self.assertTupleEqual(bitwise_xor((-1, -1, -1, -1), (1, 1, 1, 1)), (0, 0, 0, 0))

    def test_special_cases(self):
        self.assertTupleEqual(bitwise_xor((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertTupleEqual(bitwise_xor((1, 1, 1), (0, 0, 0)), (1, 1, 1))
