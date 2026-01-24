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

    def test_edge_case_n_last_element(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 2
        self.assertEqual(extract_nth_element(list1, n), [3, 6, 9])

    def test_invalid_input_n_greater_than_length(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 4
        with self.assertRaises(IndexError):
            extract_nth_element(list1, n)

    def test_invalid_input_n_negative(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        with self.assertRaises(IndexError):
            extract_nth_element(list1, n)
