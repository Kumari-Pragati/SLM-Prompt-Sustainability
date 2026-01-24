import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_combinations([]), [])

    def test_single_element_list(self):
        self.assertEqual(find_combinations([1]), [])

    def test_two_elements_list(self):
        self.assertEqual(find_combinations([1, 2]), [(3, 0), (0, 3)])

    def test_three_elements_list(self):
        self.assertEqual(find_combinations([1, 2, 3]), [(4, 0), (0, 4), (5, 0), (0, 5), (2, 1), (1, 2)])

    def test_list_with_duplicates(self):
        self.assertEqual(find_combinations([1, 2, 2, 3]), [(4, 0), (0, 4), (5, 0), (0, 5), (3, 1), (1, 3)])

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_combinations([-1, -2, 3]), [(-3, 0), (0, -3), (1, -2), (-2, 1)])
