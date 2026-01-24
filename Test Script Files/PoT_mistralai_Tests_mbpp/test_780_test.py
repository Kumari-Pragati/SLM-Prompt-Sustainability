import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(find_combinations([1, 2, 3]), [(2, 3), (1, 2), (1, 3)])

    def test_edge_case_single_element(self):
        self.assertListEqual(find_combinations([1]), [])

    def test_edge_case_two_elements(self):
        self.assertListEqual(find_combinations([1, 2]), [(1, 2)])

    def test_corner_case_empty_list(self):
        self.assertListEqual(find_combinations([]), [])
