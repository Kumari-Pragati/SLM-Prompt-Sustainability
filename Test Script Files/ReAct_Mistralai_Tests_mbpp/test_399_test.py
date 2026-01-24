import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (5, 1, 7))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(bitwise_xor((), ()), ())

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(bitwise_xor((1,), (2,)), (3,))
        self.assertEqual(bitwise_xor((2,), (1,)), (3,))

    def test_edge_case_different_length_tuples(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (1,)), (2, 3, 0))
        self.assertEqual(bitwise_xor((1, 2, 3), (1)), (2, 3, 0))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            bitwise_xor(1, 2)

    def test_error_case_mixed_types(self):
        with self.assertRaises(TypeError):
            bitwise_xor((1, 'a'), (2,))
