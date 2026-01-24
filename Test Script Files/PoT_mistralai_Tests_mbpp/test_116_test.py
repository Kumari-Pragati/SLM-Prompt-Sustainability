import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_to_int((1,)), 1)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, 2, -3)), -12)

    def test_edge_case_zero(self):
        self.assertEqual(tuple_to_int((0,)), 0)

    def test_corner_case_large_numbers(self):
        self.assertEqual(tuple_to_int((9, 8, 7, 6, 5, 4, 3, 2, 1)), 987654321)
