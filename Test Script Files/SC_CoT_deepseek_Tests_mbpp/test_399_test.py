import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 7, 5))

    def test_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_different_length_tuples(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5)), (5, 7))

    def test_large_numbers(self):
        self.assertEqual(bitwise_xor((1000000000, 2000000000), (3000000000, 4000000000)), 
                         (3000000000, 6000000000))

    def test_negative_numbers(self):
        self.assertEqual(bitwise_xor((-1, -2, -3), (-4, -5, -6)), (-5, -7, -5))

    def test_zero_and_positive(self):
        self.assertEqual(bitwise_xor((0, 1, 2), (3, 4, 5)), (3, 5, 7))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), "string")

        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), [1, 2, 3])

        with self.assertRaises(TypeError):
            bitwise_xor((1, 2, 3), {1, 2, 3})
