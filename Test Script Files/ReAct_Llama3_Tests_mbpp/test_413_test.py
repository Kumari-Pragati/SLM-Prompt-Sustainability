import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_nth_element([], 0), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_nth_element([[1, 2, 3]], 0), [1])

    def test_edge_case_invalid_index(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)

    def test_edge_case_list_with_single_element(self):
        self.assertEqual(extract_nth_element([[1]], 0), [1])

    def test_edge_case_list_with_multiple_elements(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [3, 6, 9])
