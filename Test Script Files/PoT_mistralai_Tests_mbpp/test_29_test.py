import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 3, 4, 4, 4, 5], 11), 5)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 14), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 12), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_edge_case_no_odd_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 4, 4, 4], 8), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)
