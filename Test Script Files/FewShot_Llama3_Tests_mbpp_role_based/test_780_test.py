import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_result = [(4, 6), (5, 8), (6, 10)]
        self.assertEqual(find_combinations(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = []
        self.assertEqual(find_combinations(test_list), expected_result)

    def test_single_element_list(self):
        test_list = [(1, 2)]
        expected_result = []
        self.assertEqual(find_combinations(test_list), expected_result)

    def test_list_with_duplicates(self):
        test_list = [(1, 2), (2, 3), (3, 1)]
        expected_result = [(3, 3), (4, 5)]
        self.assertEqual(find_combinations(test_list), expected_result)

    def test_list_with_non_integer_values(self):
        test_list = [('a', 'b'), ('c', 'd')]
        expected_result = [('bc', 'ad')]
        self.assertEqual(find_combinations(test_list), expected_result)
