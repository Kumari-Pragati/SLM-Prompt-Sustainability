import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 2, 1], 5), 1)

    def test_all_elements_odd(self):
        self.assertEqual(get_Odd_Occurrence([1, 3, 5, 7, 9], 5), 1)

    def test_all_elements_even(self):
        self.assertEqual(get_Odd_Occurrence([2, 4, 6, 8, 10], 5), -1)

    def test_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_array(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_array_with_duplicates(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 3], 6), 3)

    def test_array_with_duplicates_and_odd(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 3, 3, 1], 7), 1)
