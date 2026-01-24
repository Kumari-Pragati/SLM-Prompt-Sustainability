import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_sublist(self):
        self.assertEqual(extract_freq([[1, 2, 3]]), 1)

    def test_multiple_sublists(self):
        self.assertEqual(extract_freq([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), 1)

    def test_sublists_with_duplicates(self):
        self.assertEqual(extract_freq([[1, 2, 2, 3], [3, 2, 1, 1]]), 2)

    def test_sublists_with_duplicates_and_order(self):
        self.assertEqual(extract_freq([[1, 2, 2, 3], [3, 2, 1, 1], [1, 2, 3]]), 2)

    def test_sublists_with_duplicates_and_order_and_empty(self):
        self.assertEqual(extract_freq([[1, 2, 2, 3], [3, 2, 1, 1], [1, 2, 3], []]), 2)
