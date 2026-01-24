import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        expected_output = [(4, 6), (7, 8)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_single_element(self):
        test_list = [(1, 2)]
        expected_output = []
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_large_numbers(self):
        test_list = [(1000000, 2000000), (3000000, 4000000), (5000000, 6000000)]
        expected_output = [(3000000, 4000000), (7000000, 8000000)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [(-1, -2), (-3, -4), (-5, -6)]
        expected_output = [(-4, -6), (-7, -8)]
        self.assertEqual(find_combinations(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2), 'b', (5, 6)]
        with self.assertRaises(TypeError):
            find_combinations(test_list)
