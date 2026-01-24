import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_min_sum_path(self):
        self.assertEqual(min_sum_path([[2], [3, 4], [1, 5, 6]]), 5)
        self.assertEqual(min_sum_path([[1], [1, 2], [1, 2, 3]]), 3)
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 16)
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 4)
        self.assertEqual(min_sum_path([[1], [2]]), 2)
        self.assertEqual(min_sum_path([[1, 2, 3, 4, 5]]), 10)
