import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_sum_path([[1, 3, 5], [8, 2, 4], [6, 7, 3]]), 7)
        self.assertEqual(min_sum_path([[1], [2], [3]]) , 1)
        self.assertEqual(min_sum_path([[1, 1], [1, 1]]) , 1)

    def test_edge_case(self):
        self.assertEqual(min_sum_path([[1], [2], [3], [4]]) , 1)
        self.assertEqual(min_sum_path([[1, 1], [1, 1], [1, 1], [1, 1]]) , 1)
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) , 7)

    def test_corner_case(self):
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]) , 1)
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) , 7)
        self.assertEqual(min_sum_path([[1], [2], [3], [4], [5]]) , 1)
