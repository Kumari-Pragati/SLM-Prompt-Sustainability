import unittest
from mbpp_342_code import heappop, heappush
from thirtyfour_code import Node, find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_single_element(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_two_elements(self):
        self.assertEqual(find_minimum_range([[1, 2], [3, 4]]), (1, 2))

    def test_multiple_elements(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, 3))

    def test_increasing_elements(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), (1, 4))

    def test_decreasing_elements(self):
        self.assertEqual(find_minimum_range([[10, 9, 8, 7], [6, 5, 4, 3], [2, 1]]), (1, 4))

    def test_mixed_elements(self):
        self.assertEqual(find_minimum_range([[1, 5, 3], [10, 7, 6], [9, 4, 2]]), (1, 3))
