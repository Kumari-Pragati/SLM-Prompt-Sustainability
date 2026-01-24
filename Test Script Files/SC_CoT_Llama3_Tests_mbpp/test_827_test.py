import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_typical_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 12)

    def test_edge_case_empty_list(self):
        list1 = []
        C = 0
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_edge_case_column_out_of_range(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 3
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_edge_case_column_with_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = -1
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_edge_case_column_with_non_integer_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 'a'
        with self.assertRaises(TypeError):
            sum_column(list1, C)

    def test_edge_case_column_with_non_integer_index_and_non_list_input(self):
        list1 = 'not a list'
        C = 'a'
        with self.assertRaises(TypeError):
            sum_column(list1, C)

    def test_edge_case_column_with_non_integer_index_and_non_list_input_and_non_integer_column(self):
        list1 = 'not a list'
        C = 'a'
        with self.assertRaises(TypeError):
            sum_column(list1, C)
