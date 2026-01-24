import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Element([1, 7, 4, 3, 4, 8, 7], 7, 2), 7)

    def test_edge_case_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_edge_case_no_element(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_boundary_case_k_greater_than_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_boundary_case_k_equal_to_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 3), -1)

    def test_corner_case_repeated_elements(self):
        self.assertEqual(first_Element([1, 1, 1, 2, 2, 3], 6, 3), 1)

    def test_corner_case_unique_elements(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_corner_case_k_equal_to_1(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)
