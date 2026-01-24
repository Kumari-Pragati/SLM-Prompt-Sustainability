import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_simple_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_column(list1, n), [2, 5, 8])

    def test_edge_condition_empty_list(self):
        list1 = []
        n = 0
        self.assertEqual(extract_column(list1, n), [])

    def test_edge_condition_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        self.assertEqual(extract_column(list1, n), [3, 6, 9])

    def test_edge_condition_index_out_of_range(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        self.assertEqual(extract_column(list1, n), [1, 4, 7])

    def test_complex_input(self):
        list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        n = 2
        self.assertEqual(extract_column(list1, n), [3, 7, 11])
