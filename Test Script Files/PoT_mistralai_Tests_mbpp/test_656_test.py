import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 6)
        self.assertEqual(find_Min_Sum([-1, 0, 1], [-2, -1, 0], 3), 2)
        self.assertEqual(find_Min_Sum([0, 1, 2], [3, 2, 1], 3), 4)

    def test_edge_case_empty_lists(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([], [1], 1), 1)
        self.assertEqual(find_Min_Sum([1], [], 1), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Sum([1], [1], 1), 0)

    def test_edge_case_different_lengths(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2], 2), 0)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2, 3], 3), 6)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(find_Min_Sum([-1, -2, -3], [-4, -5, -6], 3), 15)
