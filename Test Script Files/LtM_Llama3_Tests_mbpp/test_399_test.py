import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(bitwise_xor((1, 2), (3, 4)), (0, 6))
        self.assertEqual(bitwise_xor((5, 6), (7, 8)), (2, 6))
        self.assertEqual(bitwise_xor((9, 10), (11, 12)), (10, 8))

    def test_empty_inputs(self):
        self.assertEqual(bitwise_xor((), ()), ())
        self.assertEqual(bitwise_xor((1, 2), ()), ())
        self.assertEqual(bitwise_xor((), (3, 4)), ())

    def test_single_element_tuples(self):
        self.assertEqual(bitwise_xor((1,), (2,)), (1,))
        self.assertEqual(bitwise_xor((3,), (4,)), (3,))
        self.assertEqual(bitwise_xor((5,), ()), ())

    def test_xor_with_self(self):
        self.assertEqual(bitwise_xor((1, 2), (1, 2)), (0, 0))
        self.assertEqual(bitwise_xor((3, 4), (3, 4)), (0, 0))
        self.assertEqual(bitwise_xor((5, 6), (5, 6)), (0, 0))

    def test_xor_with_empty(self):
        self.assertEqual(bitwise_xor((1, 2), ()), ())
        self.assertEqual(bitwise_xor((3, 4), ()), ())
        self.assertEqual(bitwise_xor((), (1, 2)), ())
        self.assertEqual(bitwise_xor((), (3, 4)), ())
