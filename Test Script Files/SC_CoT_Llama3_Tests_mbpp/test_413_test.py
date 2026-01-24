import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [2, 5, 8])

    def test_edge_case_n_zero(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_case_n_last(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 2
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [3, 6, 9])

    def test_empty_list(self):
        list1 = []
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        list1 = [[1, 2, 3]]
        n = 1
        result = extract_nth_element(list1, n)
        self.assertEqual(result, [2])

    def test_invalid_input_type(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 'a'
        with self.assertRaises(TypeError):
            extract_nth_element(list1, n)

    def test_invalid_input_value(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 10
        with self.assertRaises(IndexError):
            extract_nth_element(list1, n)
