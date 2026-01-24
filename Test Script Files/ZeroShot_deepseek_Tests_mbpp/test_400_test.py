import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element_list(self):
        self.assertEqual(extract_freq(['a']), 1)

    def test_duplicate_elements(self):
        self.assertEqual(extract_freq(['a', 'a', 'b', 'b']), 2)

    def test_sorted_list(self):
        self.assertEqual(extract_freq(['b', 'a']), 2)

    def test_unsorted_list(self):
        self.assertEqual(extract_freq(['b', 'a', 'a', 'b']), 2)

    def test_mixed_case_list(self):
        self.assertEqual(extract_freq(['a', 'A']), 2)

    def test_mixed_case_duplicate_list(self):
        self.assertEqual(extract_freq(['a', 'A', 'a', 'A']), 2)

    def test_mixed_case_unsorted_list(self):
        self.assertEqual(extract_freq(['b', 'A', 'a', 'B']), 3)
