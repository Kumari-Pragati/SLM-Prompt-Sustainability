import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_all_unique_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_large_array(self):
        self.assertEqual(find_Sum(list(range(1, 10001)), 10000), 16665000)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -2, -1], 5), -4)

    def test_mixed_numbers(self):
        self.assertEqual(find_Sum([-1, 2, -3, 2, -1], 5), 0)
