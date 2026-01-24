import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [3, 6, 9]])

    def test_edge_case_row_zero(self):
        self.assertEqual(multi_list(0, 3), [])

    def test_edge_case_col_zero(self):
        self.assertEqual(multi_list(3, 0), [])

    def test_edge_case_row_one(self):
        self.assertEqual(multi_list(1, 3), [[0, 0, 0]])

    def test_edge_case_col_one(self):
        self.assertEqual(multi_list(3, 1), [[0], [0], [0]])

    def test_edge_case_row_and_col_zero(self):
        self.assertEqual(multi_list(0, 0), [])

    def test_edge_case_row_and_col_one(self):
        self.assertEqual(multi_list(1, 1), [[0]])

    def test_edge_case_row_and_col_two(self):
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 2]])

    def test_edge_case_row_and_col_three(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [3, 6, 9]])

    def test_edge_case_row_and_col_four(self):
        self.assertEqual(multi_list(4, 4), [[0, 0, 0, 0], [0, 1, 2, 3], [4, 6, 9, 12], [12, 15, 18, 21]])
