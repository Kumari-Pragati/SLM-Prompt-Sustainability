import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 1, 3, 2]), (2, 3))

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_edge_case_no_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 3]), (1, 1) or (2, 1) or (3, 1))

    def test_corner_case_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -3]), (max(range(-1, -4)), 1))
