import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element_list(self):
        self.assertEqual(extract_freq([[1, 2, 3]]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [5, 6, 7]]), 3)

    def test_duplicates_in_list(self):
        self.assertEqual(extract_freq([[1, 2, 2], [2, 3, 3], [3, 4, 4]]), 3)

    def test_empty_sublists(self):
        self.assertEqual(extract_freq([[], [1, 2, 3], [3, 4, 5]]), 3)

    def test_empty_sublists_and_duplicates(self):
        self.assertEqual(extract_freq([[], [1, 2, 2], [2, 3, 3], [3, 4, 4]]), 3)
