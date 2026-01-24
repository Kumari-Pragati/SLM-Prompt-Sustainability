import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_column([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_column([[1]]), 1)

    def test_single_column_list(self):
        self.assertEqual(sum_column([[1], [2], [3]]), 6)

    def test_multiple_columns_list(self):
        self.assertEqual(sum_column([[1, 2], [3, 4], [5, 6]]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_column([[-1, 2], [-3, 4], [-5, 6]]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(sum_column([[1, -2], [3, 4], [-5, 6]]), 10)
