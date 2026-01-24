import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_simple_input(self):
        test_list = [(1, 2), (3, 4)]
        expected_output = [((4, 6), (5, 6))]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_empty_input(self):
        test_list = []
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_single_element_input(self):
        test_list = [(1, 2)]
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_multiple_elements_input(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_output = [((4, 6), (7, 8)), ((6, 8), (9, 10))]
        self.assertEqual(find_combinations(test_list), expected_output)
