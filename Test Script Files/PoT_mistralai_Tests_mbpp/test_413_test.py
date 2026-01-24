import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 0), [1, 4])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 1), [2, 5])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 2), [3, 6])

    def test_edge_case_empty_list(self):
        self.assertListEqual(extract_nth_element([], 0), [])

    def test_edge_case_empty_sublist(self):
        self.assertListEqual(extract_nth_element([[1], [2], [3]], 2), [])

    def test_edge_case_negative_n(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], -1), [])

    def test_edge_case_out_of_range_n(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 3), [])

    def test_corner_case_mixed_types(self):
        self.assertListEqual(extract_nth_element([[1, 'a', 3], [4, 5, 6]], 1), ['a', 5])
