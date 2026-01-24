import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_empty_table(self):
        self.assertEqual(get_maxgold([], 0, 0), 0)

    def test_single_row_single_column(self):
        self.assertEqual(get_maxgold([[1]], 1, 1), 1)

    def test_single_row_multiple_columns(self):
        self.assertEqual(get_maxgold([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 9)

    def test_multiple_rows_single_column(self):
        self.assertEqual(get_maxgold([[1], [2], [3]], 3, 1), 3)

    def test_multiple_rows_multiple_columns_diagonal(self):
        self.assertEqual(get_maxgold([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 9)

    def test_multiple_rows_multiple_columns_not_diagonal(self):
        self.assertEqual(get_maxgold([[1, 2], [3, 4]], 2, 2), 4)

    def test_negative_values(self):
        self.assertEqual(get_maxgold([[-1, 2], [3, -4]], 2, 2), 2)

    def test_zero_values(self):
        self.assertEqual(get_maxgold([[0, 2], [3, 0]], 2, 2), 3)

    def test_large_input(self):
        self.assertEqual(get_maxgold([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5, 5), 25)
