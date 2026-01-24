import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case_empty(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(find_Sum([1, 2], 2), 3)

    def test_edge_case_max_element(self):
        self.assertEqual(find_Sum([10, 20, 30, 40, 50], 5), 50)

    def test_edge_case_min_element(self):
        self.assertEqual(find_Sum([-10, -20, -30, -40, -50], 5), -10)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Sum([1, 1, 2, 2, 3, 3], 6), 6)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Sum([-10, -20, -30, -40, -50], 5), -10)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(find_Sum([-10, 1, -20, 2, -30, 3], 6), 3)
