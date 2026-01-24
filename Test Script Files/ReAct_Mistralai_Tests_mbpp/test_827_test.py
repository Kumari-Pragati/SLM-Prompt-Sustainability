import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(sum_column([]))

    def test_single_row(self):
        self.assertEqual(sum_column([[1], [2], [3]]), 6)

    def test_multiple_rows(self):
        self.assertEqual(sum_column([[1, 2], [3, 4], [5, 6]]), 21)

    def test_negative_numbers(self):
        self.assertEqual(sum_column([[-1, 2], [3, -4], [-5, 6]]), 10)

    def test_zero_index(self):
        self.assertIsNone(sum_column([[1], [2], [3]], 0))
        self.assertEqual(sum_column([[1], [2], [3]], 1), 6)

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            sum_column([[1], [2], [3]], -1)
        with self.assertRaises(IndexError):
            sum_column([[1], [2], [3]], 4)
