import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 15)

    def test_edge_case_empty_list(self):
        list1 = []
        C = 0
        self.assertEqual(sum_column(list1, C), 0)

    def test_edge_case_single_row(self):
        list1 = [[1, 2, 3]]
        C = 2
        self.assertEqual(sum_column(list1, C), 3)

    def test_edge_case_single_column(self):
        list1 = [[1], [2], [3]]
        C = 0
        self.assertEqual(sum_column(list1, C), 6)

    def test_special_case_negative_numbers(self):
        list1 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        C = 1
        self.assertEqual(sum_column(list1, C), -15)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            sum_column(None, 0)

    def test_invalid_input_empty_row(self):
        list1 = [[]]
        C = 0
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_invalid_input_negative_column_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = -1
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_invalid_input_too_large_column_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 3
        with self.assertRaises(IndexError):
            sum_column(list1, C)
