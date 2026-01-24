import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 8), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_Min([1], 0, 0), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)
        self.assertEqual(find_Min([5, 4, 3, 2, 1], 0, 4), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)

    def test_complex_cases(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9), 1)
        self.assertEqual(find_Min([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9), 1)
        self.assertEqual(find_Min([2, 1, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9), 1)
        self.assertEqual(find_Min([10, 9, 11, 12, 13, 1, 2, 3, 4, 5], 0, 9), 1)
