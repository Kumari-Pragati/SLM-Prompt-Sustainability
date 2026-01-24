import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_simple_odd_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 3, 4, 3], 7), 3)
        self.assertEqual(get_odd_occurence([4, 4, 4, 4, 4, 4, 5], 7), 5)

    def test_simple_even_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3, 4, 4, 4], 7), -1)
        self.assertEqual(get_odd_occurence([5, 5, 5, 5, 5, 5, 6], 7), -1)

    def test_empty_list(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_single_element_list(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)
        self.assertEqual(get_odd_occurence([0], 1), -1)

    def test_all_same_element(self):
        self.assertEqual(get_odd_occurence([1, 1, 1], 3), -1)
        self.assertEqual(get_odd_occurence([0, 0, 0], 3), -1)
