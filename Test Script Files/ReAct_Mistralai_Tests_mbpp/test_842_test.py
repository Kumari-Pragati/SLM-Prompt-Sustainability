import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_single_element_array(self):
        for element in [1, 2, 3, 4, 5]:
            self.assertEqual(get_odd_occurence([element], 1), element)

    def test_even_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 1, 2, 2, 3, 3, 4], 7), -1)

    def test_odd_occurrence_at_beginning(self):
        self.assertEqual(get_odd_occurence([1, 2, 1, 2, 3, 2, 3], 7), 1)

    def test_odd_occurrence_at_end(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 1, 3, 2], 7), 3)

    def test_odd_occurrence_in_middle(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 1, 3, 2, 4], 8), 4)

    def test_negative_element(self):
        self.assertEqual(get_odd_occurence([-1, -1, 1, 1, -1], 4), -1)

    def test_zero_element(self):
        self.assertEqual(get_odd_occurence([0, 0, 1, 1, 0], 5), 1)
