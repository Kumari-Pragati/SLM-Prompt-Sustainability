import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_nth_element([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_nth_element([1], 0), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_nth_element([1, 2, 3, 4], 1), [2, 4])

    def test_negative_n(self):
        self.assertListEqual(extract_nth_element([1, 2, 3, 4], -1), [3, 4])

    def test_n_greater_than_length(self):
        self.assertListEqual(extract_nth_element([1, 2, 3, 4], 5), [])

    def test_list_with_non_iterable_element(self):
        self.assertRaises(TypeError, extract_nth_element, [1, 'a', 3], 1)

    def test_list_with_non_integer_n(self):
        self.assertRaises(TypeError, extract_nth_element, [1, 2, 3], 'a')
