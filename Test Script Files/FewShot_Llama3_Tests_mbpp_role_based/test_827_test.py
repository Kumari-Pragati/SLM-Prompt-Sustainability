import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_sum_of_single_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_column(list1, 0), 12)

    def test_sum_of_multiple_columns(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_column(list1, 1), 15)

    def test_sum_of_empty_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_column(list1, 2), 0)

    def test_sum_of_column_with_negative_numbers(self):
        list1 = [[-1, 2, 3], [4, -5, 6], [7, 8, -9]]
        self.assertEqual(sum_column(list1, 0), -5)

    def test_sum_of_column_with_zero(self):
        list1 = [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
        self.assertEqual(sum_column(list1, 0), 0)
