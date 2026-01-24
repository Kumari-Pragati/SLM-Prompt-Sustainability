import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)
        self.assertEqual(find_Min([-1, -2, -3, -4, -5], 0, 4), -1)
        self.assertEqual(find_Min([10, 9, 8, 7, 6], 0, 4), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Min([1, 2, 3], 0, 2), 1)
        self.assertEqual(find_Min([1, 2, 3], 1, 2), 1)
        self.assertEqual(find_Min([1, 2, 3], 0, 0), 1)
        self.assertEqual(find_Min([1, 2, 3], 2, 2), 3)
        self.assertEqual(find_Min([], 0, 0), None)
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_complex_cases(self):
        self.assertEqual(find_Min([1, 1, 2, 3], 0, 3), 1)
        self.assertEqual(find_Min([1, 1, 2, 1], 0, 3), 1)
        self.assertEqual(find_Min([1, 1, 1, 2], 0, 3), 1)
        self.assertEqual(find_Min([2, 1, 1, 1], 0, 3), 1)
        self.assertEqual(find_Min([1, 1, 1, -1], 0, 3), -1)
