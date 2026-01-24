import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_single_element_array(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_even_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 1, 2, 2, 3, 3], 6), -1)

    def test_odd_occurrence_single_element(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3], 4), 1)

    def test_odd_occurrence_multiple_elements(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3, 4, 4, 5], 7), 5)

    def test_negative_numbers(self):
        self.assertEqual(get_odd_occurence([-1, -1, 0, 0, 1], 5), -1)

    def test_duplicate_zero(self):
        self.assertEqual(get_odd_occurence([0, 0, 1], 3), 1)

    def test_invalid_input_array(self):
        self.assertRaises(TypeError, get_odd_occurence, [1, 2, 3], 'invalid size')

    def test_invalid_input_size(self):
        self.assertRaises(TypeError, get_odd_occurence, [1, 2, 3], 0.5)
