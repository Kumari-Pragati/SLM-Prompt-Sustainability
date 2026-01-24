import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_output = [(4, 6), (7, 8), (10, 12)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_single_element(self):
        test_list = [(1, 2)]
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [(-1, 2), (3, -4), (-5, 6)]
        expected_output = [(1, 4), (3, 2), (1, 6)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_zero(self):
        test_list = [(0, 2), (3, 0), (0, 6)]
        expected_output = [(2, 2), (3, 6)]
        self.assertEqual(find_combinations(test_list), expected_output)
