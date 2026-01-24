import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 3)

    def test_edge_conditions(self):
        self.assertEqual(min_sum_path([[1]]), 1)
        self.assertEqual(min_sum_path([[1, 2, 3]]), 1)
        self.assertEqual(min_sum_path([[1, 2], [3, 4], [5, 6]]), 3)

    def test_complex_cases(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 13)
        self.assertEqual(min_sum_path([[1, 2], [3, 4], [5, 6], [7, 8]]), 12)
