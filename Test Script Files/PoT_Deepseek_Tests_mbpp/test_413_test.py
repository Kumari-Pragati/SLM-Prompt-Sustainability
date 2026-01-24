import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 5, 8])

    def test_edge_case_n_zero(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        self.assertEqual(extract_nth_element(list1, n), [1, 4, 7])

    def test_boundary_case_n_equal_to_length(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        self.assertEqual(extract_nth_element(list1, n), [3, 6, 9])

    def test_invalid_n_greater_than_length(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 4
        with self.assertRaises(IndexError):
            extract_nth_element(list1, n)

    def test_empty_list(self):
        list1 = []
        n = 0
        self.assertEqual(extract_nth_element(list1, n), [])
