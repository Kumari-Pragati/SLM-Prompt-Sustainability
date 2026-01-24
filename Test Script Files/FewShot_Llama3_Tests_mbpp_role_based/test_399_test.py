import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (3, 2, 1)
        self.assertEqual(bitwise_xor(test_tup1, test_tup2), (0, 0, 2))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(bitwise_xor(test_tup1, test_tup2), ())

    def test_tuples_of_different_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (3, 2)
        with self.assertRaises(IndexError):
            bitwise_xor(test_tup1, test_tup2)

    def test_tuples_with_non_integer_elements(self):
        test_tup1 = (1, 2, 'a')
        test_tup2 = (3, 2, 'b')
        with self.assertRaises(TypeError):
            bitwise_xor(test_tup1, test_tup2)
