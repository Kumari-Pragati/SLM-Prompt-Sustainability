import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_sum_path([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_sum_path([[1]]), 1)

    def test_simple_list(self):
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 1 + min((2, 3)))

    def test_complex_list(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         min((1 + 4 + 7, 1 + 5 + 7, 1 + 4 + 8, 2 + 4 + 6, 2 + 5 + 7, 2 + 4 + 8, 3 + 5 + 6, 3 + 4 + 7, 3 + 5 + 8, 3 + 4 + 9)))
