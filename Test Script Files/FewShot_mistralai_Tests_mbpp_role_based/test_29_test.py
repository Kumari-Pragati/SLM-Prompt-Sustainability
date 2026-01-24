import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 3, 4, 4, 4], 9), 1)

    def test_no_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 4, 4, 4], 6), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3, 3, 3, 4, 4, 4], 10), 1)

    def test_empty_list(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_list(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_single_element_list_even(self):
        self.assertEqual(get_Odd_Occurrence([2], 1), -1)
