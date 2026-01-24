import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_extract_nth_element(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [3, 6, 9])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [1, 4, 7])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [3, 6, 9])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, None), [None, None, None])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, None), [None, None, None])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6, None), [None, None, None])

    def test_extract_nth_element_empty_list(self):
        self.assertEqual(extract_nth_element([], 1), [])

    def test_extract_nth_element_empty_sublist(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [], [7, 8, 9]], 1), [1, 7, 8])
