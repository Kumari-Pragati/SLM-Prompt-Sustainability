import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_combinations([]), [])

    def test_single_element_list(self):
        self.assertEqual(find_combinations([1]), [])

    def test_two_elements(self):
        self.assertEqual(find_combinations([1, 2]), [(3, 3)])

    def test_three_elements(self):
        self.assertEqual(find_combinations([1, 2, 3]), [(4, 4), (5, 5)])

    def test_list_with_duplicates(self):
        self.assertEqual(find_combinations([1, 2, 2, 3]), [(3, 3), (4, 4)])

    def test_list_with_duplicates_and_empty(self):
        self.assertEqual(find_combinations([1, 2, 2, 3, 4]), [(3, 3), (4, 4)])

    def test_list_with_duplicates_and_empty_and_negative(self):
        self.assertEqual(find_combinations([1, 2, 2, 3, 4, -5]), [(3, 3), (4, 4)])
