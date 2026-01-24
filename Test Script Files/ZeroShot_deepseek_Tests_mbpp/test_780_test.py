import unittest
from mbpp_780_code import combinations
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_find_combinations(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_output = [(4, 6), (7, 8), (10, 12)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_find_combinations_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_find_combinations_single_element(self):
        test_list = [(1, 2)]
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_find_combinations_negative_numbers(self):
        test_list = [(-1, 2), (3, -4), (-5, 6)]
        expected_output = [(1, 4), (3, 2), (1, 6)]
        self.assertEqual(find_combinations(test_list), expected_output)
