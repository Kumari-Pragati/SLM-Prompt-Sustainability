import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_use_case(self):
        result = multi_list(3, 4)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 4)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[1][1], 1)
        self.assertEqual(result[2][2], 4)

    def test_edge_case_row_zero(self):
        result = multi_list(0, 4)
        self.assertEqual(result, [])

    def test_edge_case_col_zero(self):
        result = multi_list(4, 0)
        self.assertEqual(result, [])

    def test_edge_case_row_one(self):
        result = multi_list(1, 4)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 4)
        self.assertEqual(result[0][0], 0)

    def test_edge_case_col_one(self):
        result = multi_list(4, 1)
        self.assertEqual(len(result), 4)
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(result[0][0], 0)
