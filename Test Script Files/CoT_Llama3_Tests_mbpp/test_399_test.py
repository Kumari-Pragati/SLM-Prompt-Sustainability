import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_bitwise_xor(self):
        self.assertEqual(bitwise_xor((1,2,3), (3,2,1)), (0,0,2))
        self.assertEqual(bitwise_xor((1,2,3), (1,2,3)), (0,0,0))
        self.assertEqual(bitwise_xor((1,2,3), (2,3,1)), (1,1,2))
        self.assertEqual(bitwise_xor((1,2,3), (3,1,2)), (2,3,1))
        self.assertEqual(bitwise_xor((1,2,3), (1,1,1)), (0,1,2))
        self.assertEqual(bitwise_xor((1,2,3), (2,2,2)), (1,0,1))
        self.assertEqual(bitwise_xor((1,2,3), (3,3,3)), (2,2,2))
        self.assertEqual(bitwise_xor((1,2,3), (1,3,2)), (0,1,1))
        self.assertEqual(bitwise_xor((1,2,3), (2,1,3)), (1,3,0))
        self.assertEqual(bitwise_xor((1,2,3), (3,2,1)), (0,0,2))

    def test_bitwise_xor_empty(self):
        self.assertEqual(bitwise_xor((), ()), ())
        self.assertEqual(bitwise_xor((1,2,3), ()), ())
        self.assertEqual(bitwise_xor((), (1,2,3)), ())

    def test_bitwise_xor_diff_length(self):
        with self.assertRaises(IndexError):
            bitwise_xor((1,2,3), (1,2,3,4))

    def test_bitwise_xor_diff_type(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1,2,3), "test")
