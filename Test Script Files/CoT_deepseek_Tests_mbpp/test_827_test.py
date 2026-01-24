import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 15)

    def test_single_row(self):
        list1 = [[1, 2, 3]]
        C = 0
        self.assertEqual(sum_column(list1, C), 1)

    def test_empty_list(self):
        list1 = []
        C = 0
        self.assertEqual(sum_column(list1, C), 0)

    def test_negative_numbers(self):
        list1 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        C = 1
        self.assertEqual(sum_column(list1, C), -15)

    def test_large_numbers(self):
        list1 = [[1000000, 2000000, 3000000], [4000000, 5000000, 6000000], [7000000, 8000000, 9000000]]
        C = 1
        self.assertEqual(sum_column(list1, C), 21000000)

    def test_invalid_column_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 3
        with self.assertRaises(IndexError):
            sum_column(list1, C)
