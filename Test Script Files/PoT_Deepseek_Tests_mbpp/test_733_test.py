import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_boundary_case_single_element(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1], 2), -1)

    def test_boundary_case_multiple_same_elements(self):
        self.assertEqual(find_first_occurrence([1, 1, 1, 1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2], 2), 1)

    def test_corner_case_all_elements_same(self):
        self.assertEqual(find_first_occurrence([5, 5, 5, 5], 5), 0)

    def test_corner_case_all_elements_different(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4], 5), -1)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(find_first_occurrence([-1, -2, -3, -4], -3), 2)

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(find_first_occurrence([-1, 0, 1, 2], 0), 1)
