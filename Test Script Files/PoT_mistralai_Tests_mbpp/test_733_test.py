import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([6, 7, 8, 9, 10], 8), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1], 2), -1)

    def test_edge_case_not_present(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_corner_case_duplicate(self):
        self.assertEqual(find_first_occurrence([1, 1, 2, 3, 4, 5], 1), 0)
