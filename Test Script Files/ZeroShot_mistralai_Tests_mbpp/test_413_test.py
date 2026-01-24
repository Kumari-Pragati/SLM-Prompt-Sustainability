import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_nth_element([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_nth_element([[1]], 0), [1])

    def test_single_element_list_wrong_n(self):
        self.assertListEqual(extract_nth_element([[1]], 1), [])

    def test_list_of_lists_one_element(self):
        self.assertListEqual(extract_nth_element([[1], [2], [3]], 0), [1, 2, 3])

    def test_list_of_lists_multiple_elements(self):
        self.assertListEqual(extract_nth_element([[1, 'a'], [2, 'b'], [3, 'c']], 1), ['b', 'c'])

    def test_list_of_lists_wrong_n(self):
        self.assertListEqual(extract_nth_element([[1, 'a'], [2, 'b'], [3, 'c']], 2), [])
