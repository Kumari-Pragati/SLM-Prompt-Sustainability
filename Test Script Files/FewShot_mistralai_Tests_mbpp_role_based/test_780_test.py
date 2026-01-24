import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_two_elements(self):
        self.assertEqual(find_combinations([1, 2]), [(3, 3), (4, 4)])

    def test_three_elements(self):
        self.assertEqual(find_combinations([1, 2, 3]), [(4, 2), (5, 3), (3, 4)])

    def test_empty_list(self):
        self.assertEqual(find_combinations([]), [])

    def test_single_element(self):
        self.assertEqual(find_combinations([1]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(find_combinations([1, 1, 2]), [(3, 2), (4, 3)])
