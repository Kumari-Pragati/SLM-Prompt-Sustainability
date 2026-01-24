import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 3), (3, 1), (2, 2)]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(extract_freq([(1, 1)]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(extract_freq([(1, 1), (1, 1)]), 1)

    def test_edge_case_unsorted_list(self):
        self.assertEqual(extract_freq([(3, 1), (1, 2), (1, 3)]), 2)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            extract_freq([1, 2])
