import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 2, 2, 1, 3, 4, 4]), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(max_occurrences([1, 1]), 1)

    def test_edge_case_no_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 3]), 1 or 2 or 3)

    def test_corner_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2, -3]), -3)
