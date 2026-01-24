import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4], 5), 2)

    def test_single_element(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_all_unique(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -2, 0], 4), -2)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([1000, 1000, 1001], 3), 1000)

    def test_floats(self):
        self.assertEqual(find_Sum([1.1, 1.1, 2.2], 3), 1.1)
