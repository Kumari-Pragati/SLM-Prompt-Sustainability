import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(bitwise_xor((1,), (1,)), ())
        self.assertEqual(bitwise_xor((1,), (2,)), (1 ^ 2))
        self.assertEqual(bitwise_xor((1, 2), (1, 2)), ())
        self.assertEqual(bitwise_xor((1, 2), (3, 4)), (1 ^ 3, 2 ^ 4))

    def test_tuples_of_diff_lengths(self):
        self.assertEqual(bitwise_xor((1, 2), (1, 2, 3)), (1 ^ 1, 2 ^ 2))
        self.assertEqual(bitwise_xor((1, 2, 3), (1, 2)), (1 ^ 1, 2 ^ 2, 3 ^ 1))

    def test_tuples_with_duplicates(self):
        self.assertEqual(bitwise_xor((1, 1, 2), (1, 1, 2)), ())
        self.assertEqual(bitwise_xor((1, 1, 2), (1, 2, 3)), (1 ^ 1, 2 ^ 2))

    def test_tuples_with_non_int_elements(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1, 'a'), (1, 2))
