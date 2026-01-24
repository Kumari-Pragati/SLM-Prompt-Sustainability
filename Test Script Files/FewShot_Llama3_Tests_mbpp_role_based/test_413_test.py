import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [2, 5, 8])

    def test_edge_case_empty_list(self):
        list1 = []
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        list1 = [[1, 2, 3]]
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [2])

    def test_edge_case_invalid_n(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 4
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_n_out_of_range(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [])
