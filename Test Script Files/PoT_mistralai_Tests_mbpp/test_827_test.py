import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_typical_case(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sum_column(data, 1), 2)
        self.assertEqual(sum_column(data, 2), 15)
        self.assertEqual(sum_column(data, 3), 27)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_column([], 1), 0)

    def test_edge_case_empty_column(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sum_column(data, 4), 0)

    def test_edge_case_negative_column(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sum_column(data, -1), 0)

    def test_edge_case_out_of_range_column(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sum_column(data, len(data[0])), 24)
        self.assertEqual(sum_column(data, len(data[0]) + 1), 0)
        self.assertEqual(sum_column(data, -len(data[0])), 0)
