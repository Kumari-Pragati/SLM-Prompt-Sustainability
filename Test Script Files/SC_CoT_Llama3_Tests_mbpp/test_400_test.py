import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(extract_freq([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_freq([[1, 2, 3]]), 1)

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(extract_freq([[1], [2, 3], [4]]), 2)

    def test_edge_case_duplicates(self):
        self.assertEqual(extract_freq([[1, 2, 2], [3, 4, 5], [6, 7, 8]]), 3)

    def test_edge_case_sorted_sublists(self):
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [6, 7, 8]]), 3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            extract_freq('invalid_input')

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            extract_freq([1, 2, 3])
