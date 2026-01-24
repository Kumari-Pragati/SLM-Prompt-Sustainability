import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_simple_input(self):
        list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_minimum_range(list), (1, 9))

    def test_edge_conditions(self):
        list = [[1], [2], [3]]
        self.assertEqual(find_minimum_range(list), (1, 3))

        list = [[1, 2, 3, 4, 5]]
        self.assertEqual(find_minimum_range(list), (1, 5))

        list = [[10, 20, 30], [15, 25, 35], [27, 29, 37]]
        self.assertEqual(find_minimum_range(list), (27, 37))

    def test_complex_cases(self):
        list = [[10, 20, 30], [5, 15, 25], [11, 17, 29]]
        self.assertEqual(find_minimum_range(list), (10, 30))

        list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertEqual(find_minimum_range(list), (1, 10))

        list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(find_minimum_range(list), (1, 12))
