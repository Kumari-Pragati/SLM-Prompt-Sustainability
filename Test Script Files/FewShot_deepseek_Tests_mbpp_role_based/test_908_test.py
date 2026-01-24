import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_typical_case(self):
        arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 3)

    def test_edge_case(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 0)

    def test_boundary_case(self):
        arr = [-10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 9)

    def test_invalid_input(self):
        arr = [-10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = -1
        with self.assertRaises(ValueError):
            find_fixed_point(arr, n)
