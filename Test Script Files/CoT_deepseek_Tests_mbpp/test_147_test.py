import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 23)

    def test_single_row(self):
        tri = [[5]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 5)

    def test_empty_triangle(self):
        tri = []
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 0)

    def test_negative_numbers(self):
        tri = [[-3], [-7, -4], [-2, -4, -6], [-8, -5, -9, -3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), -3)

    def test_large_numbers(self):
        tri = [[100], [200, 150], [300, 250, 200], [400, 350, 300, 250]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 1100)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_path_sum("not a list", 4, 5)
