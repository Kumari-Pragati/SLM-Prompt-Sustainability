import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_max_path_sum(self):
        # Test case 1
        triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        self.assertEqual(max_path_sum(triangle, 4, 4), 23)

        # Test case 2
        triangle = [[1], [2, 3], [1, 5, 4], [7, 8, 9, 6]]
        self.assertEqual(max_path_sum(triangle, 4, 4), 29)

        # Test case 3
        triangle = [[10], [20, 30], [40, 50, 60], [70, 80, 90, 100]]
        self.assertEqual(max_path_sum(triangle, 4, 4), 300)

        # Test case 4
        triangle = [[-1], [-2, -3], [-4, -5, -6], [-7, -8, -9, -10]]
        self.assertEqual(max_path_sum(triangle, 4, 4), -6)

        # Test case 5
        triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        self.assertEqual(max_path_sum(triangle, 4, 4), 40)
