import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_get_maxgold_empty_list(self):
        self.assertEqual(get_maxgold([], 0, 0), 0)

    def test_get_maxgold_single_row(self):
        self.assertEqual(get_maxgold([[1]], 1, 1), 1)

    def test_get_maxgold_single_column(self):
        self.assertEqual(get_maxgold([[1, 2], [3, 4]], 2, 1), 4)

    def test_get_maxgold_small_matrix(self):
        self.assertEqual(get_maxgold([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 9)

    def test_get_maxgold_large_matrix(self):
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        self.assertEqual(get_maxgold(matrix, 5, 5), 25)
