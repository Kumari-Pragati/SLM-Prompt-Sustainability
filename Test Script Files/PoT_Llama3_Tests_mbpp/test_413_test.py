import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [1, 4, 7])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_nth_element([], 1), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_nth_element([[1, 2, 3]], 1), [1])

    def test_edge_case_invalid_n(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)

    def test_edge_case_n_out_of_range(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)

    def test_edge_case_list_with_single_element(self):
        self.assertEqual(extract_nth_element([[1]], 0), [1])

    def test_edge_case_list_with_single_element_and_invalid_n(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1]], 1)
