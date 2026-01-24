import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element(self):
        self.assertEqual(extract_freq([(1, 2)]), 1)

    def test_duplicate_elements(self):
        self.assertEqual(extract_freq([(1, 2), (1, 2)]), 1)

    def test_different_elements(self):
        self.assertEqual(extract_freq([(1, 2), (2, 3)]), 2)

    def test_mixed_elements(self):
        self.assertEqual(extract_freq([(1, 2), (2, 1), (2, 3)]), 2)

    def test_multiple_lists(self):
        self.assertEqual(extract_freq([[(1, 2), (3, 4)], [(1, 2), (3, 4)]]), 1)
