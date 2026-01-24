import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_path_sum([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(max_path_sum([[1]], 1, 0), 1)

    def test_two_elements(self):
        self.assertEqual(max_path_sum([[1, 1], [1, 1]], 2, 0), 2)

    def test_three_elements(self):
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 0), 12)

    def test_four_elements(self):
        self.assertEqual(max_path_sum([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 0), 37)

    def test_five_elements(self):
        self.assertEqual(max_path_sum([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5, 0), 64)
