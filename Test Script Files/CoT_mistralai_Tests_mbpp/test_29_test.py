import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_array(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_even_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3], 5), -1)

    def test_odd_occurrence_first_element(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 1, 3, 2], 5), 1)

    def test_odd_occurrence_middle_element(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 2], 5), 3)

    def test_odd_occurrence_last_element(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3], 5), 3)

    def test_duplicate_elements(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 2, 2, 3], 6), -1)

    def test_negative_elements(self):
        self.assertEqual(get_Odd_Occurrence([-1, -1, 1, 1, 2], 5), -1)

    def test_zero_element(self):
        self.assertEqual(get_Odd_Occurrence([0, 0, 1, 1, 2], 5), -1)
