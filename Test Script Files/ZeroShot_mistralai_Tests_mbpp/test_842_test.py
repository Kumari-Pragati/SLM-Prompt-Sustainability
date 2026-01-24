import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_single_element_list(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_even_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 1, 2], 3), -1)

    def test_odd_occurrence_single_element(self):
        self.assertEqual(get_odd_occurence([1, 2, 1], 3), 1)

    def test_odd_occurrence_multiple_elements(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3, 2, 3], 6), 3)
