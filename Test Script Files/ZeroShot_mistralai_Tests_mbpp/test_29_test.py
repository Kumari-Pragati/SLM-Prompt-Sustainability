import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_list(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_odd_occurrence_single_element(self):
        self.assertEqual(get_Odd_Occurrence([1, 1], 2), 1)

    def test_even_occurrence_single_element(self):
        self.assertEqual(get_Odd_Occurrence([2, 2], 2), -1)

    def test_multiple_elements_odd_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 4, 4, 5], 8), 5)

    def test_multiple_elements_even_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 4, 4, 4], 8), -1)
