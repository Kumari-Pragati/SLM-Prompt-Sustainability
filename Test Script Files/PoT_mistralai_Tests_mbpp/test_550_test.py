import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_Max([3, 4, 5, 6, 7], 0, 4), 5)
        self.assertEqual(find_Max([10, 9, 8, 7, 6], 0, 4), 10)
        self.assertEqual(find_Max([-1, -2, -3, -4, -5], 0, 4), -1)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_Max([], 0, 0), None)
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([1], 0, 1), 1)
        self.assertEqual(find_Max([1], 1, 1), 1)
        self.assertEqual(find_Max([1], 0, 100), 1)
        self.assertEqual(find_Max([1], 100, 1), 1)

    def test_corner_cases(self):
        self.assertEqual(find_Max([1, 1], 0, 1), 1)
        self.assertEqual(find_Max([1, 1, 2], 0, 2), 1)
        self.assertEqual(find_Max([2, 1, 1], 0, 2), 2)
        self.assertEqual(find_Max([1, 2, 1], 0, 2), 2)
        self.assertEqual(find_Max([1, 1, 1], 0, 2), 1)
        self.assertEqual(find_Max([1, 1, 1, 2], 0, 3), 1)
        self.assertEqual(find_Max([1, 1, 2, 1], 0, 3), 2)
        self.assertEqual(find_Max([1, 2, 1, 1], 0, 3), 2)
