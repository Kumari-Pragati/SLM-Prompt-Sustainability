import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element_list(self):
        self.assertEqual(extract_freq([[1]]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(extract_freq([[1, 2], [2, 3], [3, 1]]), 3)

    def test_duplicates_in_list(self):
        self.assertEqual(extract_freq([[1, 2, 2], [2, 3, 3], [3, 1, 1]]), 3)

    def test_empty_sublists(self):
        self.assertEqual(extract_freq([[], [1, 2], [2, 3], [3, 1]]), 3)

    def test_sublists_with_duplicates(self):
        self.assertEqual(extract_freq([[1, 2, 2], [2, 3, 3], [3, 1, 1]]), 3)

    def test_sublists_with_duplicates_and_empty(self):
        self.assertEqual(extract_freq([[], [1, 2, 2], [2, 3, 3], [3, 1, 1]]), 3)
