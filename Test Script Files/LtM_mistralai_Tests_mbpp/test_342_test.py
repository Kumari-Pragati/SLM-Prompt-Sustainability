import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, 9))
        self.assertEqual(find_minimum_range([[10, 20, 30], [40, 50, 60], [70, 80, 90]])), (10, 90)

    def test_edge_cases(self):
        self.assertEqual(find_minimum_range([[1, 1, 1], [1, 1, 1]]), (1, 1))
        self.assertEqual(find_minimum_range([[1000000000, 1000000000, 1000000000], [1000000000, 1000000000, 1000000000]]), (1000000000, 1000000000))
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), (1, 12))

    def test_boundary_conditions(self):
        self.assertEqual(find_minimum_range([]), (None, None))
        self.assertEqual(find_minimum_range([[]]), (None, None))
        self.assertEqual(find_minimum_range([[1]]), (1, 1))
        self.assertEqual(find_minimum_range([[1, 2], [3, 4]]), (1, 4))
