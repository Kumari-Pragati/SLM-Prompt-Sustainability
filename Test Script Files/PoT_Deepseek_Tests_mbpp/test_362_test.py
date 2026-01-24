import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_boundary_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_corner_case_repeated_elements(self):
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2]), 1)

    def test_corner_case_all_same_elements(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1]), 1)

    def test_corner_case_mixed_elements(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 3, 3]), 3)
