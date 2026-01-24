import unittest

from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 23)

    def test_edge_case(self):
        tri = [[3]]
        n = 1
        self.assertEqual(max_sum(tri, n), 3)

    def test_boundary_case(self):
        tri = [[3], [7, 4]]
        n = 2
        self.assertEqual(max_sum(tri, n), 13)

    def test_special_case(self):
        tri = [[3], [7, 0], [2, 0, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 23)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum("not a list", 4)

        with self.assertRaises(ValueError):
            max_sum([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], -1)
