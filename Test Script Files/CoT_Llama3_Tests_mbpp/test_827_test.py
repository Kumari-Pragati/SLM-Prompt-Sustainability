import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_sum_column_valid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 12)

    def test_sum_column_invalid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 'a'
        with self.assertRaises(TypeError):
            sum_column(list1, C)

    def test_sum_column_empty_list(self):
        list1 = []
        C = 0
        self.assertEqual(sum_column(list1, C), 0)

    def test_sum_column_single_element_list(self):
        list1 = [[1, 2, 3]]
        C = 1
        self.assertEqual(sum_column(list1, C), 3)

    def test_sum_column_column_out_of_range(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 3
        self.assertEqual(sum_column(list1, C), 27)
