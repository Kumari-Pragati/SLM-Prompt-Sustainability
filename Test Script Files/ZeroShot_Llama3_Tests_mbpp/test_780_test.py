import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_find_combinations(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_result = [(6, 8), (7, 10), (8, 12)]
        self.assertEqual(find_combinations(test_list), expected_result)

    def test_find_combinations_empty_list(self):
        test_list = []
        self.assertEqual(find_combinations(test_list), [])

    def test_find_combinations_single_element_list(self):
        test_list = [(1, 2)]
        self.assertEqual(find_combinations(test_list), [])

    def test_find_combinations_list_with_duplicates(self):
        test_list = [(1, 1), (2, 2), (3, 3)]
        expected_result = []
        self.assertEqual(find_combinations(test_list), expected_result)
