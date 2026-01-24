import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_result = [2, 5, 8]
        self.assertEqual(extract_nth_element(list1, n), expected_result)

    def test_edge_case_n_greater_than_length(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 4
        expected_result = [None, None, None]
        self.assertEqual(extract_nth_element(list1, n), expected_result)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 0
        expected_result = []
        self.assertEqual(extract_nth_element(list1, n), expected_result)

    def test_error_case_negative_n(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        with self.assertRaises(IndexError):
            extract_nth_element(list1, n)
