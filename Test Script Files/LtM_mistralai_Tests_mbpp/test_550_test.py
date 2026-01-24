import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Max([4, 5, 6, 3, 2], 0, 4), 6)
        self.assertEqual(find_Max([1, 2, 3], 0, 2), 3)
        self.assertEqual(find_Max([-1, -2, -3], 0, 2), -1)

    def test_edge_cases(self):
        self.assertEqual(find_Max([], 0, 0), None)
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([1, 2], 0, 1), 2)
        self.assertEqual(find_Max([1, 2], 1, 1), 2)

    def test_boundary_conditions(self):
        self.assertEqual(find_Max([-1, -2, -3], 2, 2), -1)
        self.assertEqual(find_Max([-1, -2, -3], 0, 2), -3)
        self.assertEqual(find_Max([1, 2, 3], 2, 2), 3)
        self.assertEqual(find_Max([1, 2, 3], 0, 0), 1)

    def test_complex_cases(self):
        self.assertEqual(find_Max([3, 2, 1, 4], 0, 3), 4)
        self.assertEqual(find_Max([3, 2, 1, 4], 1, 3), 4)
        self.assertEqual(find_Max([3, 2, 1, 4], 2, 3), 4)
        self.assertEqual(find_max([3, 2, 1, 4], 3, 3), 3)
