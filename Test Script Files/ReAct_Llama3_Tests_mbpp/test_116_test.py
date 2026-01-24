import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_edge_case_empty(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_to_int((5,)), 5)

    def test_edge_case_single_zero(self):
        self.assertEqual(tuple_to_int((0,)), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(tuple_to_int((-1,)), -1)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_edge_case_multiple_negative(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)

    def test_edge_case_mixed_positive_negative(self):
        self.assertEqual(tuple_to_int((1, -2, 3)), 13)

    def test_edge_case_mixed_zeros(self):
        self.assertEqual(tuple_to_int((1, 0, -2)), 10)

    def test_edge_case_mixed_positive_negative_zeros(self):
        self.assertEqual(tuple_to_int((1, 0, -2, 0)), 10)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            tuple_to_int("not a tuple")
