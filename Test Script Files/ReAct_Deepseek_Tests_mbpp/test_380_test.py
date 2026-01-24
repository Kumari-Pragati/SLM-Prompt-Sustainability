import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 1]])

    def test_edge_case_zero_rows(self):
        self.assertEqual(multi_list(0, 2), [])

    def test_edge_case_zero_cols(self):
        self.assertEqual(multi_list(2, 0), [[]]*2)

    def test_edge_case_one_row_one_col(self):
        self.assertEqual(multi_list(1, 1), [[0]])

    def test_edge_case_negative_rows(self):
        with self.assertRaises(AssertionError):
            multi_list(-1, 2)

    def test_edge_case_negative_cols(self):
        with self.assertRaises(AssertionError):
            multi_list(2, -1)

    def test_edge_case_non_integer_rows(self):
        with self.assertRaises(AssertionError):
            multi_list(2.5, 2)

    def test_edge_case_non_integer_cols(self):
        with self.assertRaises(AssertionError):
            multi_list(2, 2.5)
