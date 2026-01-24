import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_empty_triangle(self):
        self.assertEqual(max_path_sum([[]], 0, 0), 0)

    def test_single_row(self):
        self.assertEqual(max_path_sum([[1]], 1, 0), 1)
        self.assertEqual(max_path_sum([[1, 2]], 1, 1), 2)

    def test_two_rows(self):
        self.assertEqual(max_path_sum([[1, 2], [3, 4]], 2, 0), 7)
        self.assertEqual(max_path_sum([[1, 2], [3, 4]], 2, 1), 5)

    def test_larger_triangle(self):
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 0), 24)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 1), 18)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 2), 12)

    def test_negative_numbers(self):
        self.assertEqual(max_path_sum([[-1, 2, 3], [-4, -5, 6], [-7, -8, 9]], 3, 0), -1)
        self.assertEqual(max_path_sum([[-1, 2, 3], [-4, -5, 6], [-7, -8, 9]], 3, 1), 11)
        self.assertEqual(max_path_sum([[-1, 2, 3], [-4, -5, 6], [-7, -8, 9]], 3, 2), 6)

    def test_zero_dimensions( self ):
        with self.assertRaises(ValueError):
            max_path_sum([], 0, 0)

    def test_negative_m_or_n(self):
        with self.assertRaises(ValueError):
            max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 0)
        with self.assertRaises(ValueError):
            max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, -1)
