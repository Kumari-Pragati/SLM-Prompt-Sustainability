import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_max_sum(self):
        # Test case 1
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 23)

        # Test case 2
        tri = [[1], [2, 3], [1, 5, 4], [4, 1, 6, 7]]
        n = 4
        self.assertEqual(max_sum(tri, n), 18)

        # Test case 3
        tri = [[5], [7, 8], [2, 4, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 28)

        # Test case 4
        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        n = 4
        self.assertEqual(max_sum(tri, n), 34)

        # Test case 5
        tri = [[10], [20, 30], [40, 50, 60], [70, 80, 90, 100]]
        n = 4
        self.assertEqual(max_sum(tri, n), 340)
