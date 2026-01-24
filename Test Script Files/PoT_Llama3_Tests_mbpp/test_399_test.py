import unittest
from mbpp_399_code import bitwise_xor

class TestBitwiseXor(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(bitwise_xor((1, 2, 3), (4, 5, 6)), (3, 1, 7))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(bitwise_xor((), (1, 2, 3)), ())
        self.assertEqual(bitwise_xor((1, 2, 3), ()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(bitwise_xor((1,), (2,)), (3,))
        self.assertEqual(bitwise_xor((1,), ()), ())
        self.assertEqual(bitwise_xor((), (1,)), ())

    def test_edge_case_single_element_tuple_with_zero(self):
        self.assertEqual(bitwise_xor((0,), (2,)), (2,))
        self.assertEqual(bitwise_xor((0,), ()), ())
        self.assertEqual(bitwise_xor((), (0,)), ())

    def test_edge_case_single_element_tuple_with_zero_and_one(self):
        self.assertEqual(bitwise_xor((0,), (1,)), (1,))
        self.assertEqual(bitwise_xor((1,), (0,)), (1))

    def test_edge_case_single_element_tuple_with_one(self):
        self.assertEqual(bitwise_xor((1,), (1,)), (0))
        self.assertEqual(bitwise_xor((1,), ()), ())

    def test_edge_case_single_element_tuple_with_one_and_zero(self):
        self.assertEqual(bitwise_xor((1,), (0,)), (1))
        self.assertEqual(bitwise_xor((0,), (1,)), (1))

    def test_edge_case_single_element_tuple_with_one_and_one(self):
        self.assertEqual(bitwise_xor((1,), (1,)), (0))

    def test_edge_case_single_element_tuple_with_two(self):
        self.assertEqual(bitwise_xor((1,), (2,)), (3))
        self.assertEqual(bitwise_xor((2,), (1,)), (3))

    def test_edge_case_single_element_tuple_with_two_and_one(self):
        self.assertEqual(bitwise_xor((1,), (2,)), (3))
        self.assertEqual(bitwise_xor((2,), (1,)), (3))

    def test_edge_case_single_element_tuple_with_two_and_two(self):
        self.assertEqual(bitwise_xor((2,), (2,)), (0))

    def test_edge_case_single_element_tuple_with_two_and_zero(self):
        self.assertEqual(bitwise_xor((2,), (0,)), (2))
        self.assertEqual(bitwise_xor((0,), (2,)), (2))

    def test_edge_case_single_element_tuple_with_two_and_one(self):
        self.assertEqual(bitwise_xor((2,), (1,)), (3))
        self.assertEqual(bitwise_xor((1,), (2,)), (3))

    def test_edge_case_single_element_tuple_with_three(self):
        self.assertEqual(bitwise_xor((1,), (3,)), (2))
        self.assertEqual(bitwise_xor((3,), (1,)), (2))

    def test_edge_case_single_element_tuple_with_three_and_one(self):
        self.assertEqual(bitwise_xor((1,), (3,)), (2))
        self.assertEqual(bitwise_xor((3,), (1,)), (2))

    def test_edge_case_single_element_tuple_with_three_and_two(self):
        self.assertEqual(bitwise_xor((2,), (3,)), (1))
        self.assertEqual(bitwise_xor((3,), (2,)), (1))

    def test_edge_case_single_element_tuple_with_three_and_zero(self):
        self.assertEqual(bitwise_xor((3,), (0,)), (3))
        self.assertEqual(bitwise_xor((0,), (3,)), (3))

    def test_edge_case_single_element_tuple_with_three_and_one(self):
        self.assertEqual(bitwise_xor((1,), (3,)), (2))
        self.assertEqual(bitwise_xor((3,), (1,)), (2))

    def test_edge_case_single_element_tuple_with_three_and_two(self):
        self.assertEqual(bitwise_xor((2,), (3,)), (1))
        self.assertEqual(bitwise_xor((3,), (2,)), (1))

    def test_edge_case_single_element_tuple_with_three_and_zero(self):
        self.assertEqual(bitwise_xor((3,), (0,)), (3))
        self.assertEqual(bitwise_xor((0,), (3,)), (3))

    def test_edge_case_single_element_tuple_with_three_and_one(self):
        self.assertEqual(bitwise_xor((1,), (3,)), (2))
        self.assertEqual(bitwise_xor((3,), (1,)), (2))

    def test_edge_case_single_element_tuple_with_three_and_two(self):
        self.assertEqual(bitwise_xor((2,), (3,)), (1))
        self.assertEqual(bitwise_xor((3,), (2,)), (1))

    def test_edge_case_single_element_tuple_with_three_and_zero(self):
        self.assertEqual(bitwise_xor((3,), (