import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_single_sublist(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(extract_freq(test_list), 1)

    def test_multiple_sublists(self):
        test_list = [[1, 2, 3], [3, 4, 5], [1, 3, 4]]
        self.assertEqual(extract_freq(test_list), 2)

    def test_empty_sublist(self):
        test_list = [[], [1, 2, 3]]
        self.assertEqual(extract_freq(test_list), 1)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(extract_freq(test_list), 0)

    def test_single_element_sublist(self):
        test_list = [[1], [2], [3]]
        self.assertEqual(extract_freq(test_list), 3)
