import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 7, 5))

    def test_edge_conditions(self):
        self.assertEqual(bitwise_xor((), ()), ())
        self.assertEqual(bitwise_xor((1,), (1,)), ())
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6, 7)), (5, 7, 5))

    def test_complex_cases(self):
        self.assertEqual(bitwise_xor((10, 20, 30), (40, 50, 60)), (50, 70, 50))
        self.assertEqual(bitwise_xor((1, 2, 3, 4), (4, 3, 2, 1)), (5, 5, 5, 5))
