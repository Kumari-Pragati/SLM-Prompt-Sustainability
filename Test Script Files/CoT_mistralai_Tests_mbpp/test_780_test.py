import unittest
from mbpp_780_code import combinations
from 780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], find_combinations([]))

    def test_single_element_list(self):
        self.assertListEqual([], find_combinations([1]))

    def test_two_element_list(self):
        self.assertListEqual([(1, 2), (2, 1)], find_combinations([1, 2]))

    def test_three_element_list(self):
        self.assertListEqual([(1, 2), (2, 3), (1, 3)], find_combinations([1, 2, 3]))

    def test_list_with_duplicates(self):
        self.assertListEqual([(1, 1), (2, 2), (3, 3)], find_combinations([1, 2, 3, 1]))

    def test_list_with_longer_combinations(self):
        self.assertListEqual([(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)], find_combinations([1, 2, 3, 4]))

    def test_list_with_negative_numbers(self):
        self.assertListEqual([(-1, 0), (0, -1), (-1, -2), (0, -2), (-2, -1)], find_combinations([-1, 0, -2]))
