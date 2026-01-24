import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 23)

    def test_edge_case_single_row(self):
        tri = [[5]]
        n = 1
        self.assertEqual(max_sum(tri, n), 5)

    def test_edge_case_empty_triangle(self):
        tri = []
        n = 0
        self.assertEqual(max_sum(tri, n), 0)

    def test_error_case_negative_numbers(self):
        tri = [[-3], [-7, -4], [-2, -4, -6], [-8, -5, -9, -3]]
        n = 4
        self.assertEqual(max_sum(tri, n), -3)

    def test_error_case_non_integer_triangle(self):
        tri = [['3'], ['7', '4'], ['2', '4', '6'], ['8', '5', '9', '3']]
        n = 4
        with self.assertRaises(TypeError):
            max_sum(tri, n)
