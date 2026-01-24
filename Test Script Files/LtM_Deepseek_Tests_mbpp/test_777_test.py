import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 6)

    def test_edge_condition_empty_input(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(find_Sum([5], 1), 5)

    def test_boundary_condition_minimum_value(self):
        self.assertEqual(find_Sum([-1000000], 1), -1000000)

    def test_boundary_condition_maximum_value(self):
        self.assertEqual(find_Sum([1000000], 1), 1000000)

    def test_complex_input(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 11)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4], 5), 9)

    def test_negative_elements(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4], 4), -1)

    def test_sorted_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 6)

    def test_unsorted_elements(self):
        self.assertEqual(find_Sum([4, 3, 2, 1], 4), 6)
