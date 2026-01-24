import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 2, 1], 5), 1)

    def test_no_odd_occurrence(self):
        self.assertEqual(get_odd_occurrence([1, 2, 2, 3, 3], 5), -1)

    def test_empty_array(self):
        self.assertEqual(get_odd_occurrence([], 0), -1)

    def test_single_element_array(self):
        self.assertEqual(get_odd_occurrence([1], 1), 1)

    def test_all_elements_same(self):
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_all_elements_unique(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), -1)
