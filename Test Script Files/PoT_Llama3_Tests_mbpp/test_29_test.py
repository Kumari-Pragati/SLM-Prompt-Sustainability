import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_edge_case_single_element_array(self):
        self.assertEqual(get_Odd_Occurrence([1, 1], 2), 1)

    def test_edge_case_all_elements_same(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_all_elements_unique(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), -1)

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3], 5), 1)

    def test_edge_case_array_with_duplicates_and_unique(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 4], 5), 1)
