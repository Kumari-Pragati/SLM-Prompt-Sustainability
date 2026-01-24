import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_case(self):
        result = multi_list(3, 3)
        self.assertEqual(result, [[0, 0, 0], [0, 1, 2], [3, 6, 9]])

    def test_edge_case_row_zero(self):
        result = multi_list(0, 3)
        self.assertEqual(result, [])

    def test_edge_case_col_zero(self):
        result = multi_list(3, 0)
        self.assertEqual(result, [])

    def test_edge_case_row_one(self):
        result = multi_list(1, 3)
        self.assertEqual(result, [[0, 0, 0]])

    def test_edge_case_col_one(self):
        result = multi_list(3, 1)
        self.assertEqual(result, [[0], [0], [0]])

    def test_edge_case_row_col_zero(self):
        result = multi_list(0, 0)
        self.assertEqual(result, [])
