import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_nth_element([], 1), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_nth_element([[1, 2, 3]], 1), [2])

    def test_edge_case_n_out_of_range(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)

    def test_edge_case_n_negative(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            extract_nth_element("hello", 1)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "a")
