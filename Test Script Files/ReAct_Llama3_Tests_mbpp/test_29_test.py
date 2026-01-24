import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_single_odd(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), 1)

    def test_single_even(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 4, 5], 5), -1)

    def test_multiple_odd(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 3, 3, 5], 5), 1)

    def test_multiple_even(self):
        self.assertEqual(get_Odd_Occurrence([2, 2, 4, 4, 6], 5), -1)

    def test_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_array(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)

    def test_all_elements_same(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1], 5), 1)
