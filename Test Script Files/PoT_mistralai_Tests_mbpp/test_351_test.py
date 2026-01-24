import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Element([1, 2, 3, 2, 1], 5, 2), 1)
        self.assertEqual(first_Element([4, 4, 4, 4, 4], 5, 1), -1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_edge_case_single_occurrence(self):
        self.assertEqual(first_Element([1, 1], 2, 1), 1)

    def test_edge_case_multiple_occurrences(self):
        self.assertEqual(first_Element([1, 1, 2, 2, 3, 3], 6, 2), -1)

    def test_corner_case_negative_n(self):
        self.assertEqual(first_Element([1, 2, 3], -1, 1), -1)

    def test_corner_case_negative_k(self):
        self.assertEqual(first_Element([1, 2, 3], 5, -1), -1)
