import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_single_odd_element(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 1], 5), 1)

    def test_multiple_odd_elements(self):
        self.assertEqual(get_odd_occurence([1, 3, 5, 7, 9], 5), 9)

    def test_no_odd_elements(self):
        self.assertEqual(get_odd_occurence([2, 4, 6, 8], 4), -1)

    def test_empty_list(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_single_element_list(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_single_even_element(self):
        self.assertEqual(get_odd_occurence([2], 1), -1)

    def test_negative_numbers(self):
        self.assertEqual(get_odd_occurence([-1, -3, -5, -7, -9], 5), -1)

    def test_arr_size_zero(self):
        self.assertEqual(get_odd_occurence([], 0), -1)
